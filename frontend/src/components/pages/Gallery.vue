<template>
    <Layout currentPage="Galeria">
        <div class="px-lg-5">
            <div class="row py-5">
                <div class="col-lg-12 mx-auto">
                    <div class="text-white p-5 shadow-sm rounded bg-primary">
                        <h1 class="display-4">Bem-Vindo a sua galeria.</h1>
                        <p class="lead">Faça o upload de suas fotos.</p>
                        <div class="d-flex justify-content-between mb-3">
                            <label for="upload-photo" class="btn upload-button"
                                style="background-color: #fff; color: #4732bb;">Fazer Upload</label>
                            <input ref="fileInput" id="upload-photo" type="file" @change="onFileChange" accept="image/*"
                                style="display: none" multiple />
                        </div>
                        <div v-if="selectedPhotos.length > 0"
                            class="d-flex flex-wrap justify-content-center bg-white rounded"
                            style="max-height: 350px; overflow-x: hidden; overflow-y: auto;">
                            <div class="p-2 position-relative border m-2" v-for="(photo, index) in selectedPhotos"
                                :key="index">
                                <img :src="photo.url" alt="Foto selecionada" class="img-fluid"
                                    style="width: 300px; height: 300px; object-fit: contain;" />
                                <button class="btn btn-danger cancel-button rounded-circle position-absolute p-0"
                                    style="top: 20px; right: 20px;" @click="cancelSelectedPhoto(index)">
                                    <i class="fa-solid fa-trash p-2"></i>
                                </button>
                            </div>
                        </div>
                        <div v-if="uploadingProgress" class="progress mt-2">
                            <div class="progress-bar progress-bar-striped progress-bar-animated bg-info" role="progressbar"
                                :style="{ width: uploadingProgress + '%' }" aria-valuenow="100" aria-valuemin="0"
                                aria-valuemax="100">{{ uploadingProgress }} %</div>
                        </div>
                        <div v-if="selectedPhotos.length > 0" class="d-flex justify-content-center mt-3">
                            <button @click="uploadPhotos" class="btn me-2"
                                style="background-color: #fff; color: #4732bb;">Confirmar</button>
                            <button @click="clearSelectedPhotos" class="btn btn-danger">Cancelar</button>
                        </div>
                    </div>
                </div>
            </div>
            <Pagination :current-page="currentPage" :page-count="pageCount" @page-change="loadPage"
                class="d-flex justify-content-center mb-3" />
            <div class="row">
                <div v-for="photo in photos" :key="photo.id" class="col-xl-4 col-lg-4 col-md-6 mb-4">
                    <div class="card bg-white rounded shadow-sm" style="height: 430px;">
                        <div class="card-body bg-light p-0">
                            <a :href="photo.image" target="_blank">
                                <img :src="photo.image" alt="Foto" class="img-fluid card-img-top p-3"
                                    style="height: 100%; object-fit: contain;" />
                            </a>
                        </div>
                        <div class="card-footer">
                            <div class="d-flex justify-content-end">
                                <p class="small text-muted">{{ formattedDate(photo.created_at) }}</p>
                            </div>
                            <div class="d-flex align-items-center justify-content-between bg-light m-1">
                                <button v-if="!photo.is_posted" class="btn btn-primary px-3 rounded-pill font-weight-normal"
                                    @click="showPreview(photo.id)">
                                    Publicar
                                </button>
                                <button class="btn btn-secondary ml-auto px-3 rounded-pill font-weight-normal"
                                    @click="showDeleteConfirmation(photo.id)">
                                    Deletar
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <post-preview v-if="showingPreview" :showing-preview="showingPreview" :new-post="newPost" @publish="publishPhoto"
            @cancel="cancelPreview" />
        <delete-confirmation-modal :is-visible="selectedPhotoId !== null" title="Confirmação"
            message="Tem certeza que deseja excluir a imagem?" @hide="hideDeleteConfirmation" @confirm="deletePhoto" />
        <modal-error :show="responseMessage" :message="responseMessage" @close="closeModal" />
    </Layout>
</template>

<script>
import api from "@/config/api";
import CookieHelper from "@/util/cookieHelper";
import Layout from "@/components/layout/Layout.vue";
import Pagination from "@/components/layout/common/Pagination.vue";
import DeleteConfirmationModal from "@/components/layout/common/DeleteConfirmationModal.vue";
import ModalError from "@/components/err/ModalError.vue";
import PostPreview from "@/components/layout/post/PostPreview.vue";

export default {
    components: {
        Layout,
        ModalError,
        Pagination,
        DeleteConfirmationModal,
        PostPreview,
    },
    data() {
        return {
            photos: [],
            selectedPhotoId: null,
            selectedPhotos: [],
            responseMessage: null,
            showingPreview: false,
            newPost: {
                id: null,
                image: null,
                username: '',
                description: '',
            },
            currentPage: 1,
            pageCount: 1,
            info: {},
            uploadingProgress: 0,
        };
    },
    methods: {
        onFileChange(event) {
            const files = event.target.files;
            if (files && files.length > 0) {
                const maxSizeMB = 10;
                const maxSizeBytes = maxSizeMB * 1024 * 1024;

                for (let i = 0; i < files.length; i++) {
                    const file = files[i];
                    if (file.size <= maxSizeBytes) {
                        const reader = new FileReader();
                        reader.onload = (e) => {
                            this.selectedPhotos.push({
                                url: e.target.result,
                                file,
                            });
                        };
                        reader.readAsDataURL(file);
                    } else {
                        this.showErrorMessage("A imagem selecionada tem tamanho maior que o permitido.");
                    }
                }
                this.$refs.fileInput.value = "";
            }
        },
        async uploadPhotos() {
            try {
                const totalPhotos = this.selectedPhotos.length;
                this.uploadingProgress = 0;

                for (let i = 0; i < totalPhotos; i++) {
                    const photo = this.selectedPhotos[i];
                    const formData = new FormData();
                    formData.append("image", photo.file);

                    await api.post("/posts/", formData, {
                        headers: {
                            Authorization: "Bearer " + CookieHelper.getCookie("token"),
                            "Content-Type": "multipart/form-data",
                        },
                    });
                    this.uploadingProgress = Math.round(((i + 1) / totalPhotos) * 100);
                }
                this.selectedPhotos = [];
                this.fetchPhotos();
                setTimeout(() => {
                    this.uploadingProgress = 0;
                }, 3000);
            } catch (error) {
                this.showErrorMessage("Não foi possível fazer o upload das imagens.");
            }
        },
        async fetchPhotos() {
            try {
                const response = await api.get("/posts/?my_posts=true&is_posted=false", {
                    params: { page: this.currentPage },
                    headers: {
                        Authorization: "Bearer " + CookieHelper.getCookie("token"),
                    },
                });
                this.photos = response.data.results;
                this.info = response.data.info;
                this.pageCount = Math.ceil(this.info.count / this.info.per_page);
            } catch (error) {
                if (error.response && error.response.status === 500) {
                    this.showErrorMessage("Ocorreu um erro de conexão. Por favor, tente novamente mais tarde.");
                } else {
                    this.showErrorMessage("Ocorreu um erro ao listar as imagens.");
                }
                setTimeout(() => {
                    this.closeModal();
                }, 10000);
            }
        },
        async fetchUserData() {
            try {
                const response = await api.get("/users/me/", {
                    headers: {
                        Authorization: "Bearer " + CookieHelper.getCookie("token"),
                    },
                });
                if (response.status === 200 && response.data.username) {
                    this.newPost.username = response.data.username;
                }
            } catch (error) {
                this.newPost.username = "erro";
            }
        },
        async publishPhoto(post) {

            if (post.description.length > 360) {
                this.showErrorMessage("A descrição excede o limite de 360 caracteres.");
                return;
            }

            try {
                await api.patch(`/posts/${post.id}/`, { is_posted: true, description: post.description }, {
                    headers: {
                        Authorization: "Bearer " + CookieHelper.getCookie("token"),
                    },
                });
                const updatedPhoto = this.photos.find(photo => photo.id === post.id);
                if (updatedPhoto) {
                    updatedPhoto.is_posted = true;
                }
                this.cancelPreview();
                this.fetchPhotos();
            } catch (error) {
                if (error.response && error.response.status === 500) {
                    this.showErrorMessage("Ocorreu um erro de conexão. Por favor, tente novamente mais tarde.");
                } else {
                    this.showErrorMessage("Ocorreu um erro ao publicar a imagem.");
                }
                setTimeout(() => {
                    this.closeModal();
                }, 10000);
            }
        },
        async deletePhoto() {
            try {
                await api.delete(`/posts/${this.selectedPhotoId}/?is_posted=false`, {
                    headers: {
                        Authorization: "Bearer " + CookieHelper.getCookie("token"),
                    },
                });
                this.photos = this.photos.filter((photo) => photo.id !== this.selectedPhotoId);
                this.hideDeleteConfirmation();

                if (this.photos.length - 1 === 0 && this.currentPage > 1) {
                    this.currentPage--;
                }

                this.fetchPhotos();
            } catch (error) {
                if (error.response && error.response.status === 500) {
                    this.showErrorMessage("Ocorreu um erro de conexão. Por favor, tente novamente mais tarde.");
                } else {
                    this.showErrorMessage("Ocorreu um erro ao deletar a imagem.");
                }
                setTimeout(() => {
                    this.closeModal();
                }, 10000);
            }
        },
        formattedDate(date) {
            const dateformatted = new Date(date);
            return `${dateformatted.getDate()} de ${['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'][dateformatted.getMonth()]
                } de ${dateformatted.getFullYear()}`;
        },
        formatTwoDigits(number) {
            return number < 10 ? `0${number}` : number.toString();
        },
        showDeleteConfirmation(photoId) {
            this.selectedPhotoId = photoId;
            if (this.$refs.confirmDeleteModal) {
                this.$refs.confirmDeleteModal.style.display = "block";
            }
        },
        hideDeleteConfirmation() {
            this.selectedPhotoId = null;
            if (this.$refs.confirmDeleteModal) {
                this.$refs.confirmDeleteModal.style.display = "none";
            }
        },
        loadPage(page) {
            this.currentPage = page;
            this.fetchPhotos();
        },
        showPreview(photoId) {
            this.fetchUserData();
            this.showingPreview = true;
            const selectedPhoto = this.photos.find(photo => photo.id === photoId);
            if (selectedPhoto) {
                this.newPost.id = selectedPhoto.id;
                this.newPost.image = selectedPhoto.image;
            }
        },
        cancelPreview() {
            this.showingPreview = false;
            this.newPost.description = '';
        },
        showErrorMessage(message) {
            this.responseMessage = message;
        },
        clearSelectedPhotos() {
            this.selectedPhotos = [];
        },
        cancelSelectedPhoto(index) {
            this.selectedPhotos.splice(index, 1);
        },
        closeModal() {
            this.responseMessage = null;
        },
    },
    created() {
        this.fetchPhotos();
    },
};
</script>

<style scoped>
.button-hover-upload{
    background-color: #9928BF;
    color: #fff;
}
</style>