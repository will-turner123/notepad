// REPLACE the 1 in the fect with the { pid }

// Also the fetch actually gets a response from the server,
// I have no idea why the default export shit doesn't work tho
// Someone smarter than me figure this out. LOL!
import Notepad from '../components/notepad'
import { useEffect, useState } from 'react'
import { useRouter, useContext } from 'next/router'
import Base from '../components/base'
import { socket, SocketContext } from '../contexts/useSocket';

async function getNote(uuid) {
    const res = await fetch(`http://localhost:8000/api/notes/get/${uuid}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
    })
    return res.json();
}

export default function Note() {
    const router = useRouter();
    const [note, setNote] = useState(null);
    const [loading, setLoading] = useState(true);
    const connected = useContext(SocketContext);

    useEffect(() => {
        if (router.isReady && connected) {
            const uuid = router.query.uuid;
            // getNote(uuid).then((data) => {
            //     setNote(data)
            setNote(uuid)
            socket.emit('join-note', {'uuid': uuid});
                // setUuid(uuid)
            //     setLoading(false)
            // })
        }
        // TODO: connect to websocket
    }, [router.isReady, connected])

    return (
        <Base>
            {/* {note && <Notepad note={note} />} */}
            {note && <Notepad uuid={note} />}
        </Base>
    )
}
