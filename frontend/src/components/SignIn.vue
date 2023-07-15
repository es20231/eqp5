<template>
    <div class="container-lg h-100 d-flex justify-content-center align-items-center">
        <div class="card">
            <div class="card-body text-center">
                <h2 class="mb-4">Login</h2>
                <div class="row">
                    <div class="col-lg-6 col-md-8 p-0">
                        <form @submit.prevent="submitForm" class="h-100 d-flex flex-column justify-content-center mx-auto"
                            style="max-width: 350px;">
                            <div v-if="responseMessage" class="alert mb-3">
                                {{ responseMessage }}
                            </div>
                            <div class="mb-4 d-flex align-items-center">
                                <input type="email" v-model="email" class="form-control" id="email" placeholder="E-mail" />
                            </div>
                            <div class="mb-3 d-flex align-items-center">
                                <input type="password" v-model="password" class="form-control" id="password"
                                    placeholder="Senha" />
                            </div>
                            <p class="text-start">
                                <router-link to="/sign-in">Esqueci minha senha</router-link>
                            </p>
                            <button type="submit" class="btn btn-primary btn-block mb-3">Entrar</button>
                            <p class="text-center">
                                <router-link to="/sign-in">Cadastre-se</router-link>
                            </p>
                        </form>
                    </div>
                    <div class="col-lg-6 col-md-4 p-0 d-md-flex align-items-center justify-content-center">
                        <div class="card-image">
                            <img src="@/assets/img/img-login.png" alt="Imagem de Login" class="img-fluid" />
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
        document.title = "PostBook - Login";
    },
    data() {
        return {
            email: "",
            password: "",
            responseMessage: ""
        };
    },
    methods: {
        submitForm() {
            const formData = {
                email: this.email,
                password: this.password
            };
        }
    }
};
</script>