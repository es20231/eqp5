<template>
    <div class="container d-flex align-items-center justify-content-center" style="min-height: 100vh">
        <div class="col-xl-6 col-lg-6 col-md-9">
            <div class="card o-hidden border-0 shadow-lg mx-auto">
                <div class="card-body p-0">
                    <div class="p-5">
                        <div class="text-center">
                            <img :src="require('@/assets/img/img-logo.png')" alt="Logo" class="mb-2"
                                style="max-width: 60px" />
                            <h1 class="mb-4">PostBook</h1>
                        </div>
                        <form class="user mb-3">
                            <div v-if="responseMessage" :class="responseMessageType" class="alert mb-3">
                                {{ responseMessage }}
                            </div>
                            <div class="form-group mb-4">
                                <div class="input-group">
                                    <span class="input-group-text">
                                        <i class="fa-solid fa-at"></i>
                                    </span>
                                    <input type="text" class="form-control form-control-user" id="exampleInputUsername"
                                        placeholder="Nome de Usuário" v-model="username" @input="validateField('username')"
                                        :class="{ 'is-invalid': hasError('username') }" />
                                </div>
                                <div v-if="hasError('username')" class="text-danger text-right small mt-1">
                                    O nome de usuário deve conter pelo menos 3 caracteres.
                                </div>
                            </div>
                            <div class="form-group mb-4">
                                <div class="input-group">
                                    <span class="input-group-text">
                                        <i class="fa-solid fa-a"></i>
                                    </span>
                                    <input type="text" class="form-control form-control-user" id="exampleInputFullName"
                                        placeholder="Nome completo" v-model="full_name" @input="validateField('full_name')"
                                        :class="{ 'is-invalid': hasError('full_name') }" />
                                </div>
                                <div v-if="hasError('full_name')" class="text-danger text-right small mt-1">
                                    O nome deve conter pelo menos 3 caracteres.
                                </div>
                            </div>
                            <div class="form-group mb-4">
                                <div class="input-group">
                                    <span class="input-group-text">
                                        <i class="fas fa-envelope"></i>
                                    </span>
                                    <input type="email" class="form-control form-control-user" id="exampleInputEmail"
                                        placeholder="E-mail" v-model="email" @input="validateField('email')"
                                        :class="{ 'is-invalid': hasError('email') }" />
                                </div>
                                <div v-if="hasError('email')" class="text-danger text-right small mt-1">
                                    Insira um endereço de e-mail válido.
                                </div>
                            </div>
                            <div class="form-group mb-4">
                                <div class="input-group">
                                    <span class="input-group-text">
                                        <i class="fas fa-lock"></i>
                                    </span>
                                    <input type="password" class="form-control form-control-user" id="exampleInputPassword"
                                        placeholder="Senha" v-model="password" @input="validateField('password')"
                                        :class="{ 'is-invalid': hasError('password') }" />
                                </div>
                                <div v-if="hasError('password')" class="text-danger text-right small mt-1">
                                    A senha deve conter pelo menos 6 caracteres.
                                </div>
                            </div>
                            <div class="form-group mb-4">
                                <div class="input-group">
                                    <span class="input-group-text">
                                        <i class="fas fa-lock"></i>
                                    </span>
                                    <input type="password" class="form-control form-control-user"
                                        id="exampleInputConfirmPassword" placeholder="Confirme a senha"
                                        v-model="confirmPassword" @input="validateField('confirmPassword')"
                                        :class="{ 'is-invalid': hasError('confirmPassword') }" />
                                </div>
                                <div v-if="hasError('confirmPassword')" class="text-danger text-right small mt-1">
                                    As senhas não correspondem.
                                </div>
                            </div>
                            <button @click.prevent="submitForm" class="btn btn-primary btn-user btn-block">
                                Cadastrar
                            </button>
                        </form>
                        <div class="d-flex justify-content-center">
                            <div>
                                <router-link to="/" class="small">Já possui conta?</router-link>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import api from "@/config/api";
import CookieHelper from "@/util/cookieHelper";

export default {
    data() {
        return {
            username: "",
            full_name: "",
            email: "",
            password: "",
            confirmPassword: "",
            fields: ["username", "full_name", "email", "password", "confirmPassword"],
            errors: {},
            responseMessage: "",
            responseMessageType: "",
        };
    },
    methods: {
        validateField(fieldName) {
            switch (fieldName) {
                case "username":
                case "full_name":
                    this.errors[fieldName] = this[fieldName].length < 3;
                    break;
                case "email":
                    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                    this.errors[fieldName] = !emailPattern.test(this[fieldName]);
                    break;
                case "password":
                    this.errors[fieldName] = this[fieldName].length < 6;
                    this.validateField("confirmPassword");
                    break;
                case "confirmPassword":
                    this.errors[fieldName] = this.password !== this[fieldName];
                    break;
                default:
                    break;
            }
        },
        hasError(fieldName) {
            return this.errors[fieldName];
        },
        async submitForm() {
            this.errors = {};
            this.fields.forEach((field) => this.validateField(field));
            if (Object.values(this.errors).every((error) => !error)) {
                try {
                    const formData = {
                        username: this.username,
                        full_name: this.full_name,
                        email: this.email,
                        password: this.password,
                    };

                    const response = await api.post("/users/", formData);

                    if (response.status === 201) {
                        const loginResponse = await api.post("/login/", {
                            email: this.email,
                            password: this.password,
                        });

                        if (loginResponse.status === 200 && loginResponse.data.access) {
                            const token = loginResponse.data.access;
                            CookieHelper.setCookie("token", token, { secure: true });

                            this.responseMessage = "Cadastro realizado com sucesso!";
                            this.responseMessageType = "alert-success";
                            setTimeout(() => {
                                this.$router.push("/");
                            }, 3000);
                        } else {
                            this.handleLoginError();
                        }
                    } else {
                        this.handleRegistrationError();
                    }
                } catch (error) {
                    this.handleRegistrationError();
                }
            }
        },
        handleRegistrationError() {
            this.responseMessage = "Erro ao cadastrar. Por favor, tente novamente.";
            this.responseMessageType = "alert-danger";
        },
        handleLoginError() {
            this.responseMessage = "Erro ao fazer login. Por favor, tente novamente.";
            this.responseMessageType = "alert-danger";
        },
    },
};
</script>

<style scoped>
h1 {
    font-size: 2rem;
}
</style>