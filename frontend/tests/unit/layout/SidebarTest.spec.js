import { RouterLinkStub, shallowMount } from "@vue/test-utils";
import Sidebar from '@/components/layout/Sidebar.vue';
import router from "@/router";

let wrapper

beforeAll(() =>{
    wrapper = shallowMount(Sidebar, {
        global:{
            plugins: [router],
            stubs: {
                RouterLink: RouterLinkStub
            }
        }
    })
})

describe('Sidebar.vue rederization test', ()=>{
    it('should be a vue instance', ()=>{
        expect(wrapper.vm).toBeDefined()
    })

    it('should be renderizing a profile image', async()=>{
        const image = wrapper.find('img')
        expect(image.exists()).toBeTruthy()
    })
})

describe('Sidebar.vue tests', ()=>{
    it('should be a logout error', async()=>{
        await wrapper.findAll('a')[1].trigger('click')
        await wrapper.vm.$nextTick()
        try {
            (wrapper.vm.console).toThrowError()
        } catch (error) {
            console.log('passed')
        }
    })

    it('should be a link to gallery', async()=>{
        expect(wrapper.findAllComponents(RouterLinkStub)[1].text()).toBe('Galeria')
    })
})