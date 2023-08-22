import { shallowMount } from "@vue/test-utils";
import ForgotPassword from '@/components/authentication/ForgotPassword.vue';

let wrapper

beforeAll(() =>{
    wrapper = shallowMount(ForgotPassword)
})

describe('ForgotPassword.vue test in renderization web page', ()=>{
    it('should be a vue instance', ()=>{
        expect(wrapper.vm).toBeDefined()
    })

    it('the button should be rendered', ()=>{
        expect(wrapper.find('button'))
    })
})

describe('ForgotPassword.vue test with a correct input', ()=>{
    it('should be a correct email input', async() =>{
        await wrapper.setData({email: 'shibadevdog@doge.com'})
        await wrapper.vm.$nextTick()
        expect(wrapper.vm.email).toEqual("shibadevdog@doge.com")
    })
})

describe('ForgotPassword.vue test with a incorrect input', ()=>{
    it('should be a incorrect email input - 1', async()=>{
        await wrapper.setData({email: ''})
        await wrapper.vm.$nextTick()
        await wrapper.vm.submitForm()
        expect(wrapper.vm.emailError).toBe(true)
    })

    it('should be a incorrect email input - 2', async()=>{
        await wrapper.setData({email: 'shiba'})
        await wrapper.vm.$nextTick()
        await wrapper.vm.submitForm()
        expect(wrapper.vm.emailError).toBe(true)
    })

    it('should be a incorrect email input - 3', async()=>{
        await wrapper.setData({email: 'shiba@'})
        await wrapper.vm.$nextTick()
        await wrapper.vm.submitForm()
        expect(wrapper.vm.emailError).toBe(true)
    })

    it('should be a incorrect email input - 4', async()=>{
        await wrapper.setData({email: 'shiba@doge'})
        await wrapper.vm.$nextTick()
        await wrapper.vm.submitForm()
        expect(wrapper.vm.emailError).toBe(true)
    })

    it('should be a incorrect email input - 5', async()=>{
        await wrapper.setData({email: 'shiba@.com'})
        await wrapper.vm.$nextTick()
        await wrapper.vm.submitForm()
        expect(wrapper.vm.emailError).toBe(true)
    })

    it('should be a incorrect email input - 6', async()=>{
        await wrapper.setData({email: 'shiba.com'})
        await wrapper.vm.$nextTick()
        await wrapper.vm.submitForm()
        expect(wrapper.vm.emailError).toBe(true)
    })

    it('should be a incorrect email input - 7', async()=>{
        await wrapper.setData({email: '.com'})
        await wrapper.vm.$nextTick()
        await wrapper.vm.submitForm()
        expect(wrapper.vm.emailError).toBe(true)
    })

    it('should be a incorrect email input - 8', async()=>{
        await wrapper.setData({email: '@doge.com'})
        await wrapper.vm.$nextTick()
        await wrapper.vm.submitForm()
        expect(wrapper.vm.emailError).toBe(true)
    })

    it('should appear a message error', async()=>{
        await wrapper.setData({email: ''})
        await wrapper.vm.$nextTick()
        await wrapper.vm.submitForm()
            expect(wrapper.vm.emailErrorMessage).toEqual('Por favor, insira um e-mail válido.')
    })
})
