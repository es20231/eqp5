<template>
  <div class="container d-flex align-items-center justify-content-center" style="min-height: 100vh">
    <div class="col-xl-6 col-lg-6 col-md-9">
      <div class="card o-hidden border-0 shadow-lg mx-auto">
        <div class="card-body p-0">
          <div class="p-5">
            <div class="text-center">
              <img :src="require('@/assets/img/img-logo.png')" alt="Logo" class="mb-2" style="max-width: 60px" />
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
                    placeholder="Nome de Usuário" v-model="username" @input="validateUsername"
                    :class="{ 'is-invalid': usernameError }" />
                </div>
                <div v-if="usernameError" class="invalid-feedback">
                  Nome de Usuário deve conter pelo menos 3 caracteres.
                </div>
              </div>

              <div class="form-group mb-4">
                <div class="input-group">
                  <span class="input-group-text">
                    <i class="fa-solid fa-a"></i>
                  </span>
                  <input type="text" class="form-control form-control-user" id="exampleInputFullName"
                    placeholder="Nome completo" v-model="full_name" @input="validateFullName"
                    :class="{ 'is-invalid': fullNameError }" />
                </div>
                <div v-if="fullNameError" class="invalid-feedback">
                  Nome completo deve conter pelo menos 3 caracteres.
                </div>
              </div>

              <div class="form-group mb-4">
                <div class="input-group">
                  <span class="input-group-text">
                    <i class="fas fa-envelope"></i>
                  </span>
                  <input type="email" class="form-control form-control-user" id="exampleInputEmail" placeholder="E-mail"
                    v-model="email" @input="validateEmail" :class="{ 'is-invalid': emailError }" />
                </div>
                <div v-if="emailError" class="invalid-feedback">
                  Insira um endereço de e-mail válido.
                </div>
              </div>
              <div class="form-group mb-4">
                <div class="input-group">
                  <span class="input-group-text">
                    <i class="fas fa-lock"></i>
                  </span>
                  <input type="password" class="form-control form-control-user" id="exampleInputPassword"
                    placeholder="Senha" v-model="password" @input="validatePassword"
                    :class="{ 'is-invalid': passwordError }" />
                </div>
                <div v-if="passwordError" class="invalid-feedback">
                  A senha deve conter pelo menos 6 caracteres.
                </div>
              </div>
              <div class="form-group mb-4">
                <div class="input-group">
                  <span class="input-group-text">
                    <i class="fas fa-lock"></i>
                  </span>
                  <input type="password" class="form-control form-control-user" id="exampleInputConfirmPassword"
                    placeholder="Confirme a senha" v-model="confirmPassword" @input="validateConfirmPassword"
                    :class="{ 'is-invalid': confirmPasswordError }" />
                </div>
                <div v-if="confirmPasswordError" class="invalid-feedback">
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
      username: "",
      full_name: "",
      email: "",
      password: "",
      confirmPassword: "",
      usernameError: false,
      fullNameError: false,
      emailError: false,
      passwordError: false,
      confirmPasswordError: false,
      responseMessage: "",
      responseMessageType: "",
      showModal: false,
      modalTitle: "",
      modalMessage: "",
    };
  },

  methods: {
    clearAlert() {
      this.responseMessage = "";
      this.responseMessageType = "";
    },

    validateUsername() {
      this.usernameError = this.username.length < 3;
    },

    validateFullName() {
      this.fullNameError = this.full_name.length < 3;
    },

    validateEmail() {
      const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      this.emailError = !emailPattern.test(this.email);
    },

    validatePassword() {
      this.passwordError = this.password.length < 6;
      this.validateConfirmPassword();
    },

    validateConfirmPassword() {
      this.confirmPasswordError = this.password !== this.confirmPassword;
    },

    async submitForm() {
      this.validateUsername();
      this.validateFullName();
      this.validateEmail();
      this.validatePassword();
      this.validateConfirmPassword();

      const formData = {
        username: this.username,
        full_name: this.full_name,
        email: this.email,
        password: this.password,
      };

      if (
        !this.usernameError &&
        !this.fullNameError &&
        !this.emailError &&
        !this.passwordError &&
        !this.confirmPasswordError
      ) {
        try {
          const response = await api.post("/records", formData);

          if (response.status === 201) {
            this.modalTitle = "Sucesso!";
            this.modalMessage = "Cadastro realizado com sucesso!";
            this.showModal = true;
          } else {
            this.modalTitle = "Erro";
            this.modalMessage = "Erro ao cadastrar. Por favor, tente novamente.";
            this.showModal = true;
          }
        } catch (error) {
          console.error("Erro ao fazer a requisição:", error);
          this.modalTitle = "Erro";
          this.modalMessage = "Erro ao cadastrar. Por favor, tente novamente.";
          this.showModal = true;
        }

        setTimeout(() => {
          this.closeModal();
        }, 5000);
      }
    },

    closeModal() {
      this.showModal = false;
      this.modalTitle = "";
      this.modalMessage = "";
      this.username = "";
      this.full_name = "";
      this.email = "";
      this.password = "";
      this.confirmPassword = "";
      this.usernameError = false;
      this.fullNameError = false;
      this.emailError = false;
      this.passwordError = false;
      this.confirmPasswordError = false;
    },
  },
};
</script>

<style scoped>
h1 {
  font-size: 2rem;
}
</style>