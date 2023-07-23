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
        <modal-error :show="responseMessage" :message="responseMessage" @close="closeModal" />
    </div>
</template>
  
<script>
import api from "@/config/api";
import CookieHelper from "@/util/cookieHelper";
import ModalError from "@/components/err/ModalError.vue";

export default {
    components: {
        ModalError,
    },
    data() {
        return {
            email: "",
            password: "",
            responseMessage: null,
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
                    this.showErrorMessage("E-mail ou senha incorretos. Por favor, tente novamente.");
                } else {
                    this.showErrorMessage("Erro ao fazer login. Por favor, verifique sua conexão e tente novamente mais tarde.");
                }
                setTimeout(() => {
                    this.closeModal();
                }, 10000);
            }
        },
        showErrorMessage(message) {
            this.responseMessage = message;
        },
        closeModal() {
            this.responseMessage = null;
        },
    },
};
</script>
  
<style scoped>
img {
    max-width: 80px;
}
</style>