
import { AppRoot, Button, Modal, Input, Placeholder, Headline, FixedLayout, Avatar, Caption, Text, Cell, Section, ColorInput, IconContainer, Slider, List } from '@telegram-apps/telegram-ui';
import './App.css'
import '@telegram-apps/telegram-ui/dist/styles.css';
import { ModalHeader } from '@telegram-apps/telegram-ui/dist/components/Overlays/Modal/components/ModalHeader/ModalHeader';

function App() {

  return (
  <AppRoot>
    <div className="flex flex-col min-h-svh">
      <header className='bg-blue-400 h-20 text-center flex justify-start items-center pl-5'>
        <Avatar size={48} src='https://avatars.githubusercontent.com/u/84640980?v=4'></Avatar>
        <p className='pl-2 font-bold'>name</p>
        <div className='justify-end ml-auto w-22 mr-5 bg-emerald-800'>f</div>
      </header>

      <main className=' flex-1'>
        <div className='flex flex-col mt-8'>
          <Avatar size={96} className=' self-center mb-4'></Avatar>
          <p className=' font-extrabold text-2xl'>Username</p>
          <div className=' flex justify-around m-3 mt-8'>
            <div className=' flex-1 bg-[#0c0d11] border border-[#13151b] rounded-2xl py-3 px-3 flex flex-col items-start'>
              <div>
                <img src="" alt="" />0
              </div>
            </div>
            <div className=' flex-1 bg-[#0c0d11] border border-[#13151b] rounded-2xl py-3 px-3 flex flex-col items-start'>ITEM1</div>
            <div className=' flex-1 bg-[#0c0d11] border border-[#13151b] rounded-2xl py-3 px-3 flex flex-col items-start'>ITEM1</div>
          </div>
        </div>
      </main>

      <footer className='bg-blue-500 h-16 text-center flex justify-center items-center '></footer>
    </div>

  </AppRoot>
  )
}

export default App
