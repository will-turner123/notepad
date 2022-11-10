import { useState, useEffect } from 'react'

export default function Notepad({ note }) {
    const [text, setText] = useState(note.content);

    // useEffect(() => {
    //     console.log('note', note)
    //     setText(note.content)
    // }, [note])

    const handleChange = (e) => {
        setText(e.target.value)
    }

    return (
        <div id="content-body">
            <textarea 
                name="content"
                id="content"
                value={text}
                onChange={handleChange}
                sx={{
                    width: '100%',
                    height: '100%',
                }}
            />
        </div>
    )
}