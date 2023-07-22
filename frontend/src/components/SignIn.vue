<template>
    <div class="container d-flex align-items-center justify-content-center" style="min-height: 100vh;">
        <div class="col-xl-6 col-lg-6 col-md-9">
            <div class="card o-hidden border-0 shadow-lg mx-auto">
                <div class="card-body p-0">
                    <div class="p-5">
                        <div class="text-center">
                            <img src="../assets/img/img-logo.png" alt="Logo" class="mb-4" style="max-width: 80px;">
                            <h1 class="h4 text-gray-900 mb-4">PostBook</h1>
                        </div>
                        <form class="user mb-3">
                            <!-- Div de alerta para exibir a mensagem de resposta -->
                            <div v-if="responseMessage" :class="responseMessageType" class="alert mb-3">
                                {{ responseMessage }}
                            </div>
                            <div class="form-group mb-4">
                                <input type="email" class="form-control form-control-user"
                                    :class="{ 'is-invalid': emailError }" id="exampleInputEmail" aria-describedby="emailHelp"
                                    placeholder="E-mail" v-model="email" @input="validateEmail">
                            </div>
                            <div class="form-group mb-4">
                                <input type="password" class="form-control form-control-user"
                                    :class="{ 'is-invalid': passwordError }" id="exampleInputPassword" placeholder="Senha"
                                    v-model="password" @input="validatePassword">
                            </div>
                            <button @click.prevent="submitForm" class="btn btn-primary btn-user btn-block">Login</button>
                        </form>
                        <div class="d-flex justify-content-between">
                            <div>
                                <a class="small" href="forgot-password.html">Esqueceu a senha?</a>
                            </div>
                            <div>
                                <router-link to="/sign-up" class="small">Criar conta!</router-link>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    mounted() {
        document.title = "PostBook";
    },

    data() {
        return {
            email: "",
            password: "",
            emailError: false, // Variável para indicar erro no e-mail
            passwordError: false, // Variável para indicar erro na senha
            responseMessage: "",
            responseMessageType: "", // Classe dinâmica para o tipo de alerta
        };
    },

    methods: {
        clearAlert() {
            this.responseMessage = "";
            this.responseMessageType = "";
        },

        validateEmail() {
            // Validar o formato do e-mail usando uma expressão regular simples
            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            this.emailError = !emailPattern.test(this.email);
        },

        validatePassword() {
            // Validar a senha para conter pelo menos 6 caracteres
            this.passwordError = this.password.length < 6;
        },

        submitForm() {
            this.validateEmail();
            this.validatePassword();

            if (!this.emailError && !this.passwordError) {
                if (this.email === "seu-email@exemplo.com" && this.password === "sua-senha") {
                    this.responseMessage = "Login bem-sucedido!";
                    this.responseMessageType = "alert-success";
                } else {
                    this.responseMessage = "Credenciais inválidas. Por favor, tente novamente.";
                    this.responseMessageType = "alert-danger";
                }

                // Limpa o alerta após 10 segundos (10000ms)
                setTimeout(() => {
                    this.clearAlert();
                }, 10000);
            }
        }
    }
};
</script>
