<template>
    <Layout currentPage="Galeria">
        <div class="upload-container">
            <label for="upload-photo" class="btn btn-primary upload-button">
                Fazer Upload
            </label>
            <input ref="fileInput" id="upload-photo" type="file" @change="onFileChange" accept="image/*"
                style="display: none" />
        </div>
        <!-- Selected Image Card -->
        <div v-if="selectedPhoto" class="container-center">
            <div class=" card selected-photo-card">
                <img :src="selectedPhoto.url" alt="Foto selecionada" class="card-img-top selected-image" />
                <div class="card-footer button-container">
                    <button @click="uploadPhoto" class="btn btn-success confirm-button">Confirmar</button>
                    <button @click="clearSelectedPhoto" class="btn btn-danger cancel-button">Cancelar</button>
                </div>
            </div>
        </div>
        <!-- Divider and Title for Images -->
        <div class="divider"></div>
        <h3 class="images-title">Imagens na galeria (10 ultimas)</h3>
        <!-- Image Gallery -->
        <div class="card-grid-container">
            <div class="card-grid row">
                <div v-for="photo in photos" :key="photo.id" class="photo-card col-lg-4 col-md-4 col-sm-6 col-12">
                    <div class="card">
                        <a :href="photo.image" target="_blank">
                            <img :src="photo.image" alt="Foto" class="card-img-top grid-image" />
                        </a>
                        <!-- Botão de Excluir -->
                        <button class="btn btn-danger delete-button" @click="showDeleteConfirmation(photo.id)">
                            Deletar
                        </button>
                    </div>
                </div>
            </div>
        </div>
        <!-- Message if no images are posted -->
        <div v-if="photos.length === 0 && !uploading" class="no-images-message">
            Nenhuma imagem postada ainda.
        </div>

        <!-- Modal de Confirmação -->
        <div class="modal" tabindex="-1" role="dialog" id="confirmDeleteModal" v-if="selectedPhotoId !== null">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title">Confirmação</h5>
                        <button type="button" class="close" @click="hideDeleteConfirmation()">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
                        Tem certeza que deseja excluir a imagem?
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" @click="hideDeleteConfirmation()">Cancelar</button>
                        <button type="button" class="btn btn-danger" @click="deletePhoto()">Excluir</button>
                    </div>
                </div>
            </div>
        </div>
        <modal-error :show="responseMessage" :message="responseMessage" @close="closeModal" />
    </Layout>
</template>
  
<script>
import api from "@/config/api";
import CookieHelper from "@/util/cookieHelper";
import Layout from "@/components/layout/Layout.vue";
import ModalError from "@/components/err/ModalError.vue";

export default {
    components: {
        Layout,
        ModalError,
    },
    data() {
        return {
            photos: [],
            selectedPhotoId: null,
            selectedPhoto: null,
            uploading: false,
            responseMessage: null
        };
    },
    methods: {
        onFileChange(event) {
            const file = event.target.files[0];
            if (file) {
                const maxSizeMB = 10;
                const maxSizeBytes = maxSizeMB * 1024 * 1024;
                if (file.size <= maxSizeBytes) {
                    const reader = new FileReader();
                    reader.onload = (e) => {
                        this.selectedPhoto = {
                            url: e.target.result,
                            file,
                        };
                    };
                    reader.readAsDataURL(file);
                } else {
                    this.showErrorMessage("A imagem selecionada tem tamanho maior que o permitido.");
                    this.clearSelectedPhoto();
                    setTimeout(() => {
                        this.closeModal();
                    }, 10000);
                }
            } else {
                this.clearSelectedPhoto();
            }
        },
        showErrorMessage(message) {
            this.responseMessage = message;
        },
        closeModal() {
            this.responseMessage = null;
        },
        async uploadPhoto() {
            const formData = new FormData();
            formData.append("image", this.selectedPhoto.file);

            try {
                this.uploading = true;
                const response = await api.post("/posts/", formData, {
                    headers: {
                        Authorization: "Bearer " + CookieHelper.getCookie("token"),
                        "Content-Type": "multipart/form-data",
                    },
                    onUploadProgress: (progressEvent) => {
                        this.uploadProgress = Math.round((progressEvent.loaded * 100) / progressEvent.total);
                    },
                });
                this.selectedPhoto = null;
                this.fetchPhotos();
            } catch (error) {
                console.error("Error uploading photo:", error);
                this.uploading = false;
            }
        },
        clearSelectedPhoto() {
            this.selectedPhoto = null;
            this.$refs.fileInput.value = "";
        },
        async fetchPhotos() {
            try {
                const response = await api.get("/posts/?my_post=true&is_posted=false", {
                    headers: {
                        Authorization: "Bearer " + CookieHelper.getCookie("token"),
                    },
                });
                this.photos = response.data.results;
                this.clearSelectedPhoto();
            } catch (error) {
                this.showErrorMessage("Ocorreu um erro ao listar as imagens.");
                this.clearSelectedPhoto();
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
            } catch (error) {
                this.showErrorMessage("Ocorreu um erro ao deletar a imagem.");
                setTimeout(() => {
                    this.closeModal();
                }, 10000);
            }
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
    },
    created() {
        this.fetchPhotos();
    },
};
</script>

<style scoped>
.container-center {
    display: flex;
    justify-content: center;
}

.upload-container {
    display: flex;
    justify-content: flex-end;
    margin-bottom: 16px;
}

.card-grid {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
}

.card {
    height: 300px;
    width: 300px;
    margin-bottom: 20px;
    overflow: hidden;
    padding: 10px;
    position: relative;
}

.photo-card {
    margin-bottom: 15px;
}

.card-img-top {
    height: 250px;
    width: 100%;
    object-fit: cover;
    overflow: hidden;
}

.delete-button {
    position: absolute;
    bottom: 8px;
    right: 8px;
    padding: 8px 12px;
    color: white;
    background-color: rgb(192, 2, 2);
    border: none;
    border-radius: 4px;
    cursor: pointer;
    z-index: 1;
}

.delete-button:hover {
    background-color: rgb(247, 2, 2);
}

.selected-photo-card {
    position: relative;
    height: 350px;
    width: 300px;
    padding: 10px;
    overflow: hidden;
}

.button-container {
    display: flex;
    justify-content: space-between;
}

.divider {
    height: 1px;
    background-color: #ccc;
    margin: 16px 0;
}

.images-title {
    margin-bottom: 16px;
    font-size: 24px;
}

.no-images-message {
    margin-top: 16px;
    text-align: center;
    font-size: 18px;
    color: #777;
}

.card-grid-container {
    max-height: 600px;
    /* Altura máxima da div de rolagem */
    overflow-y: auto;
    /* Habilita a rolagem vertical */
    overflow-x: hidden;
}
</style>