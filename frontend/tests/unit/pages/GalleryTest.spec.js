import { RouterLinkStub, shallowMount } from "@vue/test-utils";
import Gallery from '@/components/pages/Gallery.vue';
import router from "@/router";

let wrapper

beforeAll(() =>{
    wrapper = shallowMount(Gallery, {
        global:{
            plugins: [router],
            stubs: {
                RouterLink: RouterLinkStub
            }
        }
    })
})

describe('Gallery.vue renderization test', ()=>{
    it('should be a vue instance', ()=>{
        expect(wrapper.vm).toBeDefined()
    })

    it('should be rendering the buttons', ()=>{
        expect(wrapper.findAll('button')).toBeTruthy()
    })
})

describe('Gallery.vue tests', ()=>{
    it('should be uploaded', async()=>{
        const event = {
            target:{
                files:[
                    {
                        name: 'image.png',
                        size: 50000,
                        type: 'image/png',
                    }
                ]
            }
        }

        const fileReaderSpy = jest.spyOn(FileReader.prototype, 'readAsDataURL').mockImplementation(()=> null)
        wrapper.vm.onFileChange(event)
        expect(fileReaderSpy).toHaveBeenCalledWith(event.target.files[0])
    })

    /*it('should be not uploaded', async()=>{
        const event = {
            target:{
                files:[
                    {
                        name: 'image.png',
                        size: 5000000000,
                        type: 'image/png',
                    }
                ]
            }
        }
        
        wrapper.vm.onFileChange(event)
        expect(wrapper.vm.showErrorMessage).toEqual('A imagem selecionada tem tamanho maior que o permitido.')
    })*/

    /*it('should be showed a error in fetchPhotos', async()=>{
        await wrapper.vm.fetchPhotos()
        await wrapper.vm.$nextTick()
        expect(wrapper.vm.responseMessage).toEqual('Ocorreu um erro de conexão. Por favor, tente novamente mais tarde.')
    })*/

    /*it('should be showed a error in deletePhoto', async()=>{
        await wrapper.vm.deletePhoto()
        await wrapper.vm.$nextTick()
        expect(wrapper.vm.responseMessage).toEqual('Ocorreu um erro ao deletar a imagem.')
    })*/
})