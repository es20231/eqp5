<template>
    <div class="container d-flex align-items-center justify-content-center" style="min-height: 100vh">
        <div class="col-xl-6 col-lg-6 col-md-9">
            <div class="card o-hidden border-0 shadow-lg mx-auto">
                <div class="card-body p-0">
                    <div class="p-5">
                        <div class="text-center">
                            <img :src="require('@/assets/img/img-logo.png')" alt="Logo" class="mb-2" />
                            <h1 class="text-gray-900 mb-4">PostBook</h1>
                        </div>
                        <form class="user mb-3">
                            <div class="form-group mb-3">
                                <div class="input-group">
                                    <span class="input-group-text"><i class="fa-solid fa-envelope p-1"></i></span>
                                    <input type="email" class="form-control form-control-user" :class="inputClass('email')"
                                        id="exampleInputEmail" aria-describedby="emailHelp" v-model="email"
                                        placeholder="E-mail" />
                                </div>
                                <div v-if="fieldErrors.email" class="text-danger text-right small mt-1">{{ fieldErrors.email
                                }}</div>
                            </div>
                            <div class="form-group mb-3">
                                <div class="input-group">
                                    <span class="input-group-text">
                                        <i class="fa-solid fa-lock p-1"></i>
                                    </span>
                                    <input type="password" class="form-control form-control-user"
                                        :class="inputClass('password')" id="exampleInputPassword" v-model="password"
                                        placeholder="Senha" />
                                </div>
                                <div v-if="fieldErrors.password" class="text-danger text-right small mt-1">{{
                                    fieldErrors.password }}</div>
                            </div>
                            <button @click.prevent="submitForm" class="btn btn-primary btn-user btn-block">Entrar</button>
                        </form>
                        <div class="d-flex justify-content-between">
                            <div>
                                <router-link to="/forgot-password" class="small">Esqueceu a senha?</router-link>
                            </div>
                            <div>
                                <router-link to="/sign-up" class="small">Criar conta!</router-link>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- Modal -->
        <div class="modal" v-if="responseMessage" tabindex="-1" role="dialog">
            <div class="modal-dialog modal-dialog-centered" role="document">
                <div class="modal-content">
                    <div class="modal-body" :class="responseMessageType">
                        {{ responseMessage }}
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-primary" @click="closeModal">Fechar</button>
                    </div>
                </div>
            </div>
        </div>
        <!-- End Modal -->
    </div>
</template>

<script>
import api from "@/config/api";
import CookieHelper from "@/util/cookieHelper";

export default {
    data() {
        return {
            email: "",
            password: "",
            responseMessage: "",
            responseMessageType: "",
            fieldErrors: {
                email: "",
                password: "",
            },
        };
    },
    methods: {
        validateEmail() {
            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            return emailPattern.test(this.email);
        },
        validatePassword() {
            return this.password.length >= 6;
        },
        validateForm() {
            this.fieldErrors.email = this.validateEmail() ? "" : "Por favor, insira um e-mail válido.";
            this.fieldErrors.password = this.validatePassword() ? "" : "A senha deve conter pelo menos 6 caracteres.";
        },
        inputClass(fieldName) {
            return {
                "is-invalid": this.fieldErrors[fieldName],
            };
        },
        async submitForm() {
            this.validateForm();

            if (this.fieldErrors.email || this.fieldErrors.password) {
                return;
            }

            try {
                const response = await api.post("/login/", {
                    email: this.email,
                    password: this.password,
                });

                if (response.status === 200 && response.data.access) {
                    const token = response.data.access;
                    CookieHelper.setCookie("token", token, { secure: true });

                    setTimeout(() => {
                        this.$router.push({ name: "index" });
                    }, 1000);
                }
            } catch (error) {
                if (error.response && error.response.status === 401) {
                    this.responseMessage = "E-mail ou senha incorretos. Por favor, tente novamente.";
                } else {
                    this.responseMessage = "Erro ao fazer login. Por favor, verifique sua conexão e tente novamente mais tarde.";
                }

                this.responseMessageType = "alert-danger";
                setTimeout(() => {
                    this.closeModal();
                }, 10000);
            }
        },
        closeModal() {
            this.responseMessage = "";
            this.responseMessageType = "";
        },
    },
};
</script>

<style scoped>
img {
    max-width: 80px;
}

.modal {
    display: block;
    background-color: rgba(0, 0, 0, 0.5);
}

.modal-dialog {
    margin-top: 10vh;
}

.alert-success {
    background-color: #d4edda;
    color: #155724;
}

.alert-danger {
    background-color: #ffffff;
    color: #721c24;
}
</style>