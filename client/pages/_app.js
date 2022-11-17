import '../styles/globals.css'
import '98.css'
import { SocketProvider, useSocket } from '../contexts/useSocket';

function MyApp({ Component, pageProps }) {
  
  return (
    <SocketProvider>
      <Component {...pageProps} />
    </SocketProvider>
  )
}

export default MyApp
