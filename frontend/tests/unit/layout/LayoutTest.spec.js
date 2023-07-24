import { config, shallowMount } from "@vue/test-utils";
import Layout from '@/components/layout/Layout.vue';
import Sidebar from '@/components/layout/Sidebar.vue';
import Navbar from '@/components/layout/Navbar.vue';

let wrapper, wr

beforeAll(() =>{
    wrapper = shallowMount(Layout,{
        props:{
            currentPage: ''
        }
    })
})

describe('Layout.vue renderization test', ()=>{
    it('should be a vue instance', ()=>{
        expect(wrapper.vm).toBeDefined()
    })
})

describe('Layout.vue test', ()=>{
    it('should be new value in props currentPage', async()=>{
        await wrapper.setProps({currentPage: 'test'})
        await wrapper.vm.$nextTick()
        expect(wrapper.props().currentPage).toEqual('test')
    })

    it('Sidebar and Navbar should be rendered', ()=>{
        const sidebar = wrapper.findComponent(Sidebar)
        const navbar = wrapper.findComponent(Navbar)
        expect(sidebar.exists()).toBeTruthy()
        expect(navbar.exists()).toBeTruthy()
    })

    it('isSmallScreen should be true', async()=>{
        await wrapper.setData({isSmallScreen: true})
        await wrapper.vm.$nextTick()
        expect(wrapper.vm.isSmallScreen).toBeTruthy()
    })
})