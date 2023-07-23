<template>
    <div class="modal" v-if="show" tabindex="-1" role="dialog">
        <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content">
                <div class="modal-body">
                    {{ message }}
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-primary" @click="closeModal">Fechar</button>
                </div>
            </div>
        </div>
    </div>
</template>
  
<script>
export default {
    props: {
        show: {
            type: Boolean,
            required: true,
        },
        message: {
            type: String,
            required: true,
        },
    },
    methods: {
        closeModal() {
            this.$emit("close");
        },
    },
};
</script>