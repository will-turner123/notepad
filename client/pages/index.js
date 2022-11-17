// import styles from '../styles/Home.module.css'
import Base from '../components/base'
import Footer from '../components/footer'
import Notepad from '../components/notepad'
import Link from 'next/link'

export default function Home() {
  return (
    <Base>
      <Link href="/create">Make a new note?</Link> 
    </Base>
  )
}
