<template>
    <div v-if="showingPreview" class="post-preview">
        <div class="post mb-4">
            <div class="user-info mb-1">
                <img :src="require('@/assets/img/img-user.png')" alt="Foto do Usuário"
                    class="user-profile-picture border border-primary rounded-circle" />
                <span class="username">{{ newPost.username }}</span>
            </div>
            <textarea v-model="newPost.description" class="form-control mb-2" rows="4" placeholder="Insira uma descrição"
                maxlength="360"></textarea>
            <div v-if="newPost.description.length > 360" class="error-message">
                A descrição não pode ter mais de 1000 caracteres.
            </div>
            <img :src="newPost.image" alt="Foto selecionada" class="post-image mt-auto" />
            <div class="post-actions">
                <span class="like-button">
                    <i class="fas fa-heart"></i> 0
                </span>
                <span class="dislike-button">
                    <i class="fas fa-thumbs-down"></i> 0
                </span>
                <span class="comment-button">
                    <i class="fas fa-comment"></i> 0
                </span>
            </div>
            <div class="post-preview-buttons mt-2">
                <button @click="publishPhoto(newPost)" class="btn btn-success">Confirmar</button>
                <button @click="cancelPreview" class="btn btn-danger">Cancelar</button>
            </div>
        </div>
    </div>
</template>
  
<script>
export default {
    props: {
        showingPreview: Boolean,
        newPost: Object,
    },
    methods: {
        publishPhoto(post) {
            this.$emit("publish", post);
        },
        cancelPreview() {
            this.$emit("cancel");
        },
    },
};
</script>
  
<style scoped>
.post-preview {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
}

.post-preview-buttons {
    display: flex;
    justify-content: flex-end;
    margin-top: 10px;
    gap: 10px
}
</style>