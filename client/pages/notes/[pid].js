// REPLACE the 1 in the fect with the { pid }

// Also the fetch actually gets a response from the server,
// I have no idea why the default export shit doesn't work tho
// Someone smarter than me figure this out. LOL!
import Notepad from '../../components/notepad'
import { useEffect, useState } from 'react'

async function getNote() {
    const res = await fetch('http://localhost:8000/api/notes/1/', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
    })
    return res.json();
}

export default function render_note() {
    const [note, setNote] = useState(null);
    const [loading, setLoading] = useState(true);
    // this should be moved to a component
    useEffect(() => {
        getNote().then((data) => {
            setNote(data)
            setLoading(false)
        })
    }, [])

    return (
        <>
            {loading ? <div>Loading...</div> : <Notepad note={note} />}
        </>
    )
}