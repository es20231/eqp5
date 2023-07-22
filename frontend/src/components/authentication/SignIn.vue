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
                                    <input type="email" class="form-control form-control-user"
                                        :class="{ 'is-invalid': emailError }" id="exampleInputEmail"
                                        aria-describedby="emailHelp" placeholder="E-mail" v-model="email"
                                        @input="validateEmail" />
                                </div>
                                <div v-if="emailError" class="text-danger text-right small mt-1">{{ emailErrorMessage }}
                                </div>
                            </div>
                            <div class="form-group mb-3">
                                <div class="input-group">
                                    <span class="input-group-text"><i class="fa-solid fa-lock p-1"></i></span>
                                    <input type="password" class="form-control form-control-user"
                                        :class="{ 'is-invalid': passwordError }" id="exampleInputPassword"
                                        placeholder="Senha" v-model="password" @input="validatePassword" />
                                </div>
                                <div v-if="passwordError" class="text-danger text-right small mt-1">{{ passwordErrorMessage
                                }}</div>
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

export default {
    data() {
        return {
            email: "",
            password: "",
            emailError: false,
            passwordError: false,
            emailErrorMessage: "",
            passwordErrorMessage: "",
            responseMessage: "",
            responseMessageType: "",
        };
    },

    methods: {
        clearAlert() {
            this.responseMessage = "";
            this.responseMessageType = "";
        },

        validateEmail() {
            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            this.emailError = !emailPattern.test(this.email);
            this.emailErrorMessage = this.emailError ? "Insira um e-mail válido." : "";
        },

        validatePassword() {
            this.passwordError = this.password.length < 6;
            this.passwordErrorMessage = this.passwordError ? "A senha deve conter pelo menos 6 caracteres." : "";
        },

        async submitForm() {
            this.validateEmail();
            this.validatePassword();

            if (!this.emailError && !this.passwordError) {
                try {
                    const response = await api.post("/login", {
                        email: this.email,
                        password: this.password,
                    });

                    if (response.status === 200 && response.data.success) {
                        this.responseMessage = "Login bem-sucedido!";
                        this.responseMessageType = "alert-success";
                        setTimeout(() => {
                            this.closeModal();
                            this.$router.push('/index');
                        }, 3000);
                    } else {
                        this.responseMessage = "Credenciais inválidas. Por favor, tente novamente.";
                        this.responseMessageType = "alert-danger";
                    }
                } catch (error) {
                    this.responseMessage = "Erro ao fazer login. Por favor, tente novamente mais tarde.";
                    this.responseMessageType = "alert-danger";
                }

                // Clear the alert after 5 seconds (5000ms)
                setTimeout(() => {
                    this.clearAlert();
                }, 5000);

                this.emailErrorMessage = "";
                this.passwordErrorMessage = "";
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

/* Estilos personalizados para o modal */
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