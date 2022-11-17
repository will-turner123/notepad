import Notepad from '../components/notepad'
import { useEffect, useState } from 'react'
import { useRouter, useContext } from 'next/router'
import Base from '../components/base'
import { socket } from '../components/socket';


export default function Note() {
    const router = useRouter();
    const [note, setNote] = useState(null);
    const [loading, setLoading] = useState(true);
    // const connected = useContext(SocketContext);

    useEffect(() => {
        if (router.isReady) {
            const uuid = router.query.uuid;

            setNote(uuid)
            // socket.emit('join-note', {'uuid': uuid});

        }
    }, [router.isReady])

    return (
        <Base>
            {/* {note && <Notepad note={note} />} */}
            {note && <Notepad uuid={note} />}
        </Base>
    )
}
