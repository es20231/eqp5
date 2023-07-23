<template>
    <div class="container d-flex align-items-center justify-content-center" style="min-height: 100vh;">
        <div class="col-xl-6 col-lg-6 col-md-9">
            <div class="card o-hidden border-0 shadow-lg mx-auto">
                <div class="card-body p-0">
                    <div class="p-5">
                        <div class="text-center">
                            <img :src="require('@/assets/img/img-logo.png')" alt="Logo" class="mb-1"
                                style="max-width: 80px;">
                            <h1 class="text-gray-900 mb-0">PostBook</h1>
                        </div>
                        <form class="user mb-1">
                            <p class="text-center small">Enviaremos um e-mail para redefinir sua senha. Pegue a sua senha
                                temporária e faça o login com ela.</p>
                            <div class="form-group mb-4">
                                <div class="input-group">
                                    <span class="input-group-text">
                                        <i class="fa-solid"
                                            :class="{ 'fa-check-circle text-success': showConfirmation, 'fa-envelope p-1': !showConfirmation }"></i>
                                    </span>
                                    <input type="email" class="form-control form-control-user"
                                        :class="{ 'is-invalid': emailError }" id="exampleInputEmail"
                                        aria-describedby="emailHelp" placeholder="E-mail" v-model="email"
                                        @input="validateEmail">
                                </div>
                                <div v-if="emailError" class="text-danger text-right small mt-1">{{ emailErrorMessage }}
                                </div>
                            </div>
                            <button @click.prevent="submitForm" class="btn btn-primary btn-user btn-block mb-2"
                                :disabled="loading || showResendButton">
                                <span v-if="loading">
                                    <i class="fa-solid fa-spinner-third fa-spin"></i> Enviando...
                                </span>
                                <span v-else>{{ buttonText }}</span>
                            </button>
                        </form>
                        <div class="d-flex justify-content-center">
                            <div>
                                <router-link to="/" class="small">Voltar para o login</router-link>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <UserNotFoundErrorModal v-if="!userExists" :show="!userExists" @close="userExists = true" />
    </div>
</template>
  
<script>
import UserNotFoundErrorModal from '@/components/err/UserNotFoundErrorModal.vue';
import api from '@/config/api';

export default {
    components: {
        UserNotFoundErrorModal,
    },
    data() {
        return {
            email: "",
            emailError: false,
            emailErrorMessage: "",
            loading: false,
            showResendButton: false,
            timeRemaining: 30,
            showConfirmation: false,
            userExists: true,
        };
    },
    computed: {
        buttonText() {
            if (this.loading) {
                return "Enviando...";
            } else if (this.showResendButton) {
                return `Reenviar (${this.timeRemaining} s)`;
            } else {
                return "Recuperar Senha";
            }
        },
    },
    methods: {
        validateEmail() {
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            this.emailError = !emailRegex.test(this.email);
            this.emailErrorMessage = this.emailError ? "Por favor, insira um e-mail válido." : "";
        },
        async submitForm() {
            this.validateEmail();

            if (!this.emailError) {
                this.loading = true;
                this.startResendTimer();

                try {
                    await api.post('/users/forgot-password/', { email: this.email });
                    this.showConfirmation = true;
                    setTimeout(() => {
                        this.showConfirmation = false;
                    }, 3000);
                    this.userExists = true;
                } catch (error) {
                    if (error.response && error.response.status === 404) {
                        this.userExists = false;
                    } else {
                        console.error(error);
                    }
                } finally {
                    this.loading = false;
                }
            }
        },
        clearEmailError() {
            this.emailError = false;
            this.emailErrorMessage = "";
        },
        startResendTimer() {
            this.showResendButton = true;
            this.timeRemaining = 30;
            this.timer = setInterval(() => {
                if (this.timeRemaining > 0) {
                    this.timeRemaining--;
                } else {
                    clearInterval(this.timer);
                    this.showResendButton = false;
                }
            }, 1000);
        },
        resendEmail() {
            this.showResendButton = false;
            this.submitForm();
        },
    },
};
</script>