// REPLACE the 1 in the fect with the { pid }

// Also the fetch actually gets a response from the server,
// I have no idea why the default export shit doesn't work tho
// Someone smarter than me figure this out. LOL!
import Notepad from '../../components/notepad'

async function getNote() {
    const res = await fetch('http://localhost:8000/api/notes/1', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
    })
    return res.json();
}

export default function render_note() {
    const note = getNote();
    return (
        <Notepad />
    )
}