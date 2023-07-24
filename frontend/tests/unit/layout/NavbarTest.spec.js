import { shallowMount } from "@vue/test-utils";
import Navbar from '@/components/layout/Navbar.vue';

let wrapper

beforeAll(() =>{
    wrapper = shallowMount(Navbar,{
        props:{
            currentPage: ''
        }
    })
})

describe('Navbar.vue renderization test', ()=>{
    it('should be rendered', ()=>{
        expect(wrapper.vm).toBeDefined()
    })

    it('the button should be found', ()=>{
        const button = wrapper.find('button')
        expect(button.exists()).toBeTruthy()
    })
})

describe('Navbar.vue tests', ()=>{
    it('should be a username different of error', async()=>{
        await wrapper.setData({username:'shibaDevDog'})
        await wrapper.vm.$nextTick()
        expect(wrapper.vm.username).toEqual('shibaDevDog')
    })

    it('should be a error usermane', async()=>{
        await wrapper.vm.fetchUserData()
        await wrapper.vm.$nextTick()
        expect(wrapper.vm.username).toEqual('erro')
    })

    it('should be a currentPage string different of empty', async()=>{
        await wrapper.setProps({currentPage: 'test'})
        await wrapper.vm.$nextTick()
        expect(wrapper.props().currentPage).toEqual('test')
    })

    it("the show data should be true", async()=>{
        await wrapper.vm.toggleSidebar()
        await wrapper.vm.$nextTick()
        expect(wrapper.vm.show).toBeTruthy()
    })
})