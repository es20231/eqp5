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
                                <span v-else-if="showResendButton">
                                    <i class="fa-solid fa-clock"></i> Reenviar ({{ timeRemaining }} s)
                                </span>
                                <span v-else>Recuperar Senha</span>
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
    </div>
</template>
  
<script>
import api from '@/config/api';

export default {
    data() {
        return {
            email: "",
            emailError: false,
            emailErrorMessage: "",
            loading: false,
            showResendButton: false,
            timeRemaining: 30,
            showConfirmation: false,
        };
    },

    methods: {
        validateEmail() {
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            this.emailError = !emailRegex.test(this.email);
            this.emailErrorMessage = this.emailError ? "Por favor, insira um e-mail válido." : "";
        },

        submitForm() {
            this.validateEmail();

            if (!this.emailError) {
                this.loading = true;
                this.startResendTimer();

                api.post('/users/forgot-password/', { email: this.email })
                    .then((response) => {
                        this.showConfirmation = true;
                        setTimeout(() => {
                            this.showConfirmation = false;
                        }, 3000);
                    })
                    .catch((error) => {
                        console.error(error);
                    })
                    .finally(() => {
                        this.loading = false;
                    });
            }
        },

        closeModal() {
            this.showModal = false;
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
  
<style scoped>
/* Estilos personalizados para o modal */
.modal-header {
    background-color: #5845C4;
    color: white;
}

.modal {
    display: block;
    background-color: rgba(0, 0, 0, 0.5);
}

.modal-dialog {
    margin-top: 10vh;
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    display: flex;
    align-items: flex-start;
}
</style>