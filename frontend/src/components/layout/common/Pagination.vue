<template>
    <nav v-if="pageCount > 1">
        <ul class="pagination pagination-flat m-0">
            <!-- <li class="page-item" v-if="pageCount > 5">
                <a class="page-link" href="#" @click="previousFivePages">
                    <i class="fa-solid fa-angle-double-left"></i>
                    <span class="sr-only">Previous 5 Pages</span>
                </a>
            </li> -->
            <li class="page-item">
                <a class="page-link" href="#" aria-label="Previous" @click="previousPage">
                    <i class="fa-solid fa-arrow-left"></i>
                    <span class="sr-only">Previous</span>
                </a>
            </li>
            <li v-for="page in visiblePages" :key="page" :class="['page-item', { 'active': page === currentPage }]">
                <a class="page-link" href="#" @click="changePage(page)">{{ page }}</a>
            </li>
            <li class="page-item">
                <a class="page-link" href="#" aria-label="Next" @click="nextPage">
                    <i class="fa-solid fa-arrow-right"></i>
                    <span class="sr-only">Next</span>
                </a>
            </li>
            <!-- <li class="page-item" v-if="currentPage <= pageCount - 5">
                <a class="page-link" href="#" @click="nextFivePages">
                    <i class="fa-solid fa-angle-double-right"></i>
                    <span class="sr-only">Next 5 Pages</span>
                </a>
            </li> -->
        </ul>
    </nav>
</template>
  
<script>
export default {
    props: {
        currentPage: {
            type: Number,
            required: true
        },
        pageCount: {
            type: Number,
            required: true
        }
    },
    computed: {
        visiblePages() {
            let startPage = Math.max(Math.floor((this.currentPage - 1) / 5) * 5 + 1, 1);
            let endPage = Math.min(startPage + 4, this.pageCount);

            if (this.currentPage >= this.pageCount - 1) {
                startPage = Math.max(this.pageCount - 4, 1);
                endPage = this.pageCount;
            }

            const pages = [];
            for (let i = startPage; i <= endPage; i++) {
                pages.push(i);
            }

            return pages;
        }
    },
    methods: {
        previousPage() {
            if (this.currentPage > 1) {
                this.$emit('page-change', this.currentPage - 1);
            }
        },
        nextPage() {
            if (this.currentPage < this.pageCount) {
                this.$emit('page-change', this.currentPage + 1);
            }
        },
        changePage(page) {
            this.$emit('page-change', page);
        },
        // previousFivePages() {
        //     const previousFive = Math.max(this.currentPage - 5, 1);
        //     this.$emit('page-change', previousFive);
        // },
        // nextFivePages() {
        //     const nextFive = Math.min(this.currentPage + 5, this.pageCount);
        //     this.$emit('page-change', nextFive);
        // }
    }
};
</script>