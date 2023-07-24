import { shallowMount } from "@vue/test-utils";
import ModalError from '@/components/err/ModalError.vue';

let wrapper

beforeAll(() =>{
    wrapper = shallowMount(ModalError,{
        props:{
            show: false,
            message: ''
        }
    })
})

describe('ModalError.vue renderization test', ()=>{
    it('should be a vue instance', ()=>{
        expect(wrapper.vm).toBeDefined()
    })
})

describe('ModalError.vue test', ()=>{
    it('should be show a message', async()=>{
        await wrapper.setProps({message: 'test'})
        await wrapper.vm.$nextTick()
        expect(wrapper.props().message).toBe('test')
    })

    it('should be show something', async()=>{
        await wrapper.setProps({show: true})
        await wrapper.vm.$nextTick()
        expect(wrapper.props().show).toBe(true)
    })

    it('should be close the modal', async()=>{
        await wrapper.vm.closeModal()
        await wrapper.vm.$nextTick()
        expect(wrapper.emitted('close')).toBeTruthy()
    })
})