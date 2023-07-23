import { shallowMount } from "@vue/test-utils";
import SignIn from '@/components/authentication/SignIn.vue';

    let wrapper

    beforeAll(() =>{
        wrapper = shallowMount(SignIn)
    })

describe('SignIn.vue tests in renderization of web page', () =>{

    it('should be a vue instance', () =>{
        expect(wrapper.vm).toBeDefined()
    })

    it('the button should be rendered', ()=>{
        expect(wrapper.find('button'))
    })
})

describe('SignIn.vue tests in a correct inputs', () =>{

    it('should update inputs when values is changed',async() =>{
        await wrapper.setData({ email: 'shibadevdog@doge.com' })
        await wrapper.vm.$nextTick()
        expect(wrapper.vm.email).toEqual('shibadevdog@doge.com')
        await wrapper.setData({ password: 'roofroofattack08' })
        await wrapper.vm.$nextTick()
        expect(wrapper.vm.password).toEqual('roofroofattack08')
    })

})

describe('SignIn.vue tests in input email', () =>{

    it('there should be an error in the email input - 1', async() =>{
        await wrapper.setData({email: 'shiba'})
        await wrapper.vm.$nextTick()
        await wrapper.setData({password: 'roofroofattack08'})
        await wrapper.vm.$nextTick()
        await wrapper.vm.submitForm()
        expect(wrapper.vm.fieldErrors.email).toEqual('Por favor, insira um e-mail válido.')
    })

    it('there should be an error in the email input - 2', async() =>{
        await wrapper.setData({email: 'shiba@'})
        await wrapper.vm.$nextTick()
        await wrapper.setData({password: 'roofroofattack08'})
        await wrapper.vm.$nextTick()
        await wrapper.vm.submitForm()
        expect(wrapper.vm.fieldErrors.email).toEqual('Por favor, insira um e-mail válido.')
    })

    it('there should be an error in the email input - 3', async() =>{
        await wrapper.setData({email: 'shiba@doge'})
        await wrapper.vm.$nextTick()
        await wrapper.setData({password: 'roofroofattack08'})
        await wrapper.vm.$nextTick()
        await wrapper.vm.submitForm()
        expect(wrapper.vm.fieldErrors.email).toEqual('Por favor, insira um e-mail válido.')
    })

    it('there should be an error in the email input - 4', async() =>{
        await wrapper.setData({email: 'shiba@.com'})
        await wrapper.vm.$nextTick()
        await wrapper.setData({password: 'roofroofattack08'})
        await wrapper.vm.$nextTick()
        await wrapper.vm.submitForm()
        expect(wrapper.vm.fieldErrors.email).toEqual('Por favor, insira um e-mail válido.')
    })

    it('there should be an error in the email input - 5', async() =>{
        await wrapper.setData({email: 'shiba.com'})
        await wrapper.vm.$nextTick()
        await wrapper.setData({password: 'roofroofattack08'})
        await wrapper.vm.$nextTick()
        await wrapper.vm.submitForm()
        expect(wrapper.vm.fieldErrors.email).toEqual('Por favor, insira um e-mail válido.')
    })

    it('there should be an error in the email input - 6', async() =>{
        await wrapper.setData({email: '@doge.com'})
        await wrapper.vm.$nextTick()
        await wrapper.setData({password: 'roofroofattack08'})
        await wrapper.vm.$nextTick()
        await wrapper.vm.submitForm()
        expect(wrapper.vm.fieldErrors.email).toEqual('Por favor, insira um e-mail válido.')
    })

    it('there should be an error in the email input - 7', async() =>{
        await wrapper.setData({email: ''})
        await wrapper.vm.$nextTick()
        await wrapper.setData({password: 'roofroofattack08'})
        await wrapper.vm.$nextTick()
        await wrapper.vm.submitForm()
        expect(wrapper.vm.fieldErrors.email).toEqual('Por favor, insira um e-mail válido.')
    }) 

})

describe('SignIn.vue test in input password', () => {

    it('there should be an error in the password input - 1', async() =>{
        await wrapper.setData({email:'shibadevdog@doge.com'})
        await wrapper.vm.$nextTick()
        await wrapper.setData({password: 'roof'})
        await wrapper.vm.$nextTick()
        await wrapper.vm.submitForm()
        expect(wrapper.vm.fieldErrors.password).toEqual('A senha deve conter pelo menos 6 caracteres.')
    })

    it('there should be an error in the password input - 2', async() =>{
        await wrapper.setData({email:'shibadevdog@doge.com'})
        await wrapper.vm.$nextTick()
        await wrapper.setData({password: ''})
        await wrapper.vm.$nextTick()
        await wrapper.vm.submitForm()
        expect(wrapper.vm.fieldErrors.password).toEqual('A senha deve conter pelo menos 6 caracteres.')
    })


})

describe('SignIn.vue tests in 401 message error', () =>{

    it('should appear a pop-up message for 401 error', async() =>{
        await wrapper.setData({email: 'shibadevdog@doge.com'})
        await wrapper.vm.$nextTick()
        await wrapper.setData({password: 'roofroofattack08'})
        await wrapper.vm.$nextTick()
        await wrapper.vm.submitForm()
        expect(wrapper.vm.responseMessage).toEqual('Erro ao fazer login. Por favor, verifique sua conexão e tente novamente mais tarde.')
    })

    it('should appear a type of alert in message for 401 error', async() =>{
        await wrapper.setData({email: 'shibadevdog@doge.com'})
        await wrapper.vm.$nextTick()
        await wrapper.setData({password: 'roofroofattack08'})
        await wrapper.vm.$nextTick()
        await wrapper.vm.submitForm()
        expect(wrapper.vm.responseMessageType).toEqual('alert-danger')
    })
})
