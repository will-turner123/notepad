import { useRouter } from 'next/router'

async function save_note(pid) {
    let url = 'http://localhost:8000/api/notes/save/'
    if (pid != -1) {
        url += pid
    }
    const res = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
    })
    console.log('successfully saved');
    return res.json();
}

export default function Footer() {
    const router = useRouter()
    const { pid } = router.query
    
    return (
        <div class="footer">
            <button id="save-btn" onClick={save_note}>Save</button>
        </div>
    )
}