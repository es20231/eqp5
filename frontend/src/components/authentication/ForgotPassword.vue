<template>
  <div class="container d-flex align-items-center justify-content-center" style="min-height: 100vh;">
    <div class="col-xl-6 col-lg-6 col-md-9">
      <div class="card o-hidden border-0 shadow-lg mx-auto">
        <div class="card-body p-0">
          <div class="p-5">
            <div class="text-center">
              <img :src="require('@/assets/img/img-logo.png')" alt="Logo" class="mb-2" style="max-width: 80px;">
              <h1 class="text-gray-900">PostBook</h1>
            </div>
            <form class="user mb-1">
              <p class="text-center">Enviaremos um e-mail para redefinir sua senha.</p>
              <div class="form-group mb-4">
                <div class="input-group">
                  <span class="input-group-text">
                    <i class="fa-solid fa-envelope p-1"></i>
                  </span>
                  <input type="email" class="form-control form-control-user" :class="{ 'is-invalid': emailError }"
                    id="exampleInputEmail" aria-describedby="emailHelp" placeholder="E-mail" v-model="email"
                    @input="validateEmail">
                </div>
                <div v-if="emailError" class="text-danger text-right small mt-1">{{ emailErrorMessage }}</div>
              </div>
              <button @click.prevent="submitForm" class="btn btn-primary btn-user btn-block mb-2">Recuperar Senha</button>
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

    <!-- Modal -->
    <div class="modal" v-if="showModal" tabindex="-1" role="dialog">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Confirmação</h5>
            <button type="button" class="close" @click="closeModal">
              <span>&times;</span>
            </button>
          </div>
          <div class="modal-body">
            Um e-mail de recuperação de senha foi enviado para: <strong>{{ email }}</strong>.
          </div>
        </div>
      </div>
    </div>
    <!-- End Modal -->
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
      showModal: false,
      loading: false, // Add a loading state
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
        this.loading = true; // Show loading state while waiting for the API response

        api.post('/enviar-email-recuperacao', { email: this.email })
          .then((response) => {
            // Lógica para lidar com a resposta da API, se necessário
            this.showModal = true;

            // Fecha o modal após 10 segundos (10000ms)
            setTimeout(() => {
              this.closeModal();
            }, 10000);
          })
          .catch((error) => {
            console.error(error);
          })
          .finally(() => {
            this.loading = false; // Hide loading state after API response
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