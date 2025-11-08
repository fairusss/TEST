
import { AppRoot, Button, Modal, Input, Placeholder, Headline, FixedLayout, Avatar, Caption, Text, Cell, Section, ColorInput, IconContainer, Slider, List, Divider } from '@telegram-apps/telegram-ui';
import './App.css'
import '@telegram-apps/telegram-ui/dist/styles.css';
import tonlogo from './assets/ton_symbol.svg'
import { ModalHeader } from '@telegram-apps/telegram-ui/dist/components/Overlays/Modal/components/ModalHeader/ModalHeader';

function App() {

  return (
  <AppRoot>
    <div className="flex flex-col min-h-svh">
      <header className='h-20 text-center flex justify-start items-center pl-5'>
        <Avatar size={48} src='https://avatars.githubusercontent.com/u/84640980?v=4'></Avatar>
        <p className='pl-2 font-bold'>name</p>
        <div className='flex justify-between ml-auto w-28 h-7 mr-5 bg-emerald-800 rounded-md p-1 whitespace-nowrap'>
          <img src={tonlogo} alt="" className=''/>
          <p className=''>0 TON</p>
          <img src={tonlogo} alt="" className=''/>
        </div>
      </header>
      <Divider></Divider>
      
      <main className='flex-1'>

      </main>

      <footer className='bg-blue-500 h-16 text-center flex justify-center items-center '></footer>
    </div>

  </AppRoot>
  )
}

export default App
