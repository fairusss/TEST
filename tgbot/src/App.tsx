
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

      <main className='flex-1'></main>

      <footer className='bg-blue-500 h-16 text-center flex justify-center items-center '></footer>
    </div>

  </AppRoot>
  )
}

export default App
