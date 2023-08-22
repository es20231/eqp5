<template>
    <div class="modal" tabindex="-1" role="dialog" v-if="isVisible">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">{{ title }}</h5>
                    <button type="button" class="close" @click="hideModal">
                        <span aria-hidden="true" style="color: #fff;">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    {{ message }}
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-primary" @click="hideModal">{{ cancelButtonText }}</button>
                    <button type="button" class="btn btn-danger" @click="confirmAction">{{ confirmButtonText }}</button>
                </div>
            </div>
        </div>
    </div>
</template>
  
<script>
export default {
    props: {
        isVisible: {
            type: Boolean,
            required: true
        },
        title: {
            type: String,
            required: true
        },
        message: {
            type: String,
            required: true
        },
        cancelButtonText: {
            type: String,
            default: "Cancelar"
        },
        confirmButtonText: {
            type: String,
            default: "Excluir"
        }
    },
    methods: {
        hideModal() {
            this.$emit("hide");
        },
        confirmAction() {
            this.$emit("confirm");
            this.hideModal();
        }
    }
};
</script>