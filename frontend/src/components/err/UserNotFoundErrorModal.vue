<template>
    <div class="modal fade show d-block">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">Usuário não encontrado</h5>
                    <button type="button" class="close" @click="$emit('close')" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    O e-mail informado não pertence a um usuário cadastrado. Verifique o e-mail digitado ou crie uma conta.
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-primary" @click="$emit('close')">Fechar</button>
                </div>
            </div>
        </div>
    </div>
</template>
  
<script>
export default {
    props: {
        show: Boolean,
    },
};
</script>