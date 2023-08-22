import { shallowMount } from "@vue/test-utils";
import SignUp from '@/components/authentication/SignUp.vue';

let wrapper

beforeAll(() =>{
    wrapper = shallowMount(SignUp)
})

describe('SignUp.vue test in renderization of web page', ()=>{
    it('should be a vue instance', ()=>{
        expect(wrapper.vm).toBeDefined()
    })

    it('the button should be rendered', () =>{
        expect(wrapper.find('button'))
    })
})

describe('SignUp.vue test with correct inputs', () =>{
    it('should be passed completly', async()=>{
        await wrapper.setData({username: 'shibaDeDog'})
        await wrapper.vm.$nextTick()
        await wrapper.setData({full_name: 'Shibalderson da Silva'})
        await wrapper.vm.$nextTick()
        await wrapper.setData({email: 'shibadevdog@doge.com'})
        await wrapper.vm.$nextTick()
        await wrapper.setData({password: 'roofroofattack08'})
        await wrapper.vm.$nextTick()
        await wrapper.setData({confirmPassword: 'roofroofattack08'})
        await wrapper.vm.$nextTick()
        expect(wrapper.vm.username).toEqual('shibaDeDog')
        expect(wrapper.vm.full_name).toEqual('Shibalderson da Silva')
        expect(wrapper.vm.email).toEqual('shibadevdog@doge.com')
        expect(wrapper.vm.password).toEqual('roofroofattack08')
        expect(wrapper.vm.confirmPassword).toEqual('roofroofattack08')
    })
})

describe('SignUp.vue test with a incorrect username', () =>{
    it('should be an error in username input - 1', async() =>{
        await wrapper.setData({username: ""})
        await wrapper.vm.$nextTick()
        await wrapper.vm.submitForm()
        expect(wrapper.vm.errors['username']).toBe(true)
    })

    it('should be an error in username input - 2', async() =>{
        await wrapper.setData({username: 'sh'})
        await wrapper.vm.$nextTick()
        await wrapper.vm.submitForm()
        expect(wrapper.vm.errors['username']).toBe(true)
    })
})

describe('SignUp.vue test with a incorrect full name', ()=>{
    it('should be an error in full name input - 1', async() =>{
        await wrapper.setData({full_name: ""})
        await wrapper.vm.$nextTick()
        await wrapper.vm.submitForm()
        expect(wrapper.vm.errors['full_name']).toBe(true)
    })

    it('should be an error in full name input - 2', async() =>{
        await wrapper.setData({full_name: 'sh'})
        await wrapper.vm.$nextTick()
        await wrapper.vm.submitForm()
        expect(wrapper.vm.errors['full_name']).toBe(true)
    })
})

describe('SignUp.vue test with a incorrect email', ()=>{
    it('should be an error in email input - 1', async() =>{
        await wrapper.setData({email: 'shiba'})
        await wrapper.vm.$nextTick()
        await wrapper.vm.submitForm()
        expect(wrapper.vm.errors['email']).toBe(true)
    })

    it('should be an error in email input - 2', async() =>{
        await wrapper.setData({email: 'shiba@'})
        await wrapper.vm.$nextTick()
        await wrapper.vm.submitForm()
        expect(wrapper.vm.errors['email']).toBe(true)
    })

    it('should be an error in email input - 3', async() =>{
        await wrapper.setData({email: 'shiba@doge'})
        await wrapper.vm.$nextTick()
        await wrapper.vm.submitForm()
        expect(wrapper.vm.errors['email']).toBe(true)
    })

    it('should be an error in email input - 4', async() =>{
        await wrapper.setData({email: 'shiba@.com'})
        await wrapper.vm.$nextTick()
        await wrapper.vm.submitForm()
        expect(wrapper.vm.errors['email']).toBe(true)
    })

    it('should be an error in email input - 5', async() =>{
        await wrapper.setData({email: 'shiba.com'})
        await wrapper.vm.$nextTick()
        await wrapper.vm.submitForm()
        expect(wrapper.vm.errors['email']).toBe(true)
    })

    it('should be an error in email input - 6', async() =>{
        await wrapper.setData({email: '@doge.com'})
        await wrapper.vm.$nextTick()
        await wrapper.vm.submitForm()
        expect(wrapper.vm.errors['email']).toBe(true)
    })

    it('should be an error in email input - 7', async() =>{
        await wrapper.setData({email: ''})
        await wrapper.vm.$nextTick()
        await wrapper.vm.submitForm()
        expect(wrapper.vm.errors['email']).toBe(true)
    })

    it('should be an error in email input - 8', async() =>{
        await wrapper.setData({email: '.com'})
        await wrapper.vm.$nextTick()
        await wrapper.vm.submitForm()
        expect(wrapper.vm.errors['email']).toBe(true)
    })
})

describe('SignUp.vue test with a incorrect password input', () =>{
    it('should be an error in password input - 1', async() =>{
        await wrapper.setData({password: ''})
        await wrapper.vm.$nextTick()
        await wrapper.vm.submitForm()
        expect(wrapper.vm.errors['password']).toBe(true)
    })

    it('should be an error in password input - 2', async() =>{
        await wrapper.setData({password: 'dfkt'})
        await wrapper.vm.$nextTick()
        await wrapper.vm.submitForm()
        expect(wrapper.vm.errors['password']).toBe(true)
    })
})

describe('SignUp.vue test with a incorrect confirm password input', () =>{
    it('should be an error in confirm password input', async() =>{
        await wrapper.setData({confirmPassword: ''})
        await wrapper.vm.$nextTick()
        await wrapper.vm.submitForm()
        expect(wrapper.vm.errors['confirmPassword']).toBe(true)
    })

    it('should be an error in confirm password input', async() =>{
        await wrapper.setData({confirmPassword: '24345'})
        await wrapper.vm.$nextTick()
        await wrapper.vm.submitForm()
        expect(wrapper.vm.errors['confirmPassword']).toBe(true)
    })

    it('should be an error in confirm password input', async() =>{
        await wrapper.setData({password: 'roofroofattack08'})
        await wrapper.vm.$nextTick()
        await wrapper.setData({confirmPassword: 'roofroof'})
        await wrapper.vm.$nextTick()
        await wrapper.vm.submitForm()
        expect(wrapper.vm.errors['confirmPassword']).toBe(true)
    })
})

describe('SignUp.vue test with a response message', ()=>{
    it('should be an error in response of sign up', async() =>{
        await wrapper.setData({username: 'shibaDeDog'})
        await wrapper.vm.$nextTick()
        await wrapper.setData({full_name: 'Shibalderson da Silva'})
        await wrapper.vm.$nextTick()
        await wrapper.setData({email: 'shibadevdog@doge.com'})
        await wrapper.vm.$nextTick()
        await wrapper.setData({password: 'roofroofattack08'})
        await wrapper.vm.$nextTick()
        await wrapper.setData({confirmPassword: 'roofroofattack08'})
        await wrapper.vm.$nextTick()
        await wrapper.vm.submitForm()
        expect(wrapper.vm.responseMessage).toEqual('Erro ao cadastrar. Por favor, verifique sua conexão e tente novamente mais tarde.')
    })
})

