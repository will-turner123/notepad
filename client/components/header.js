import Link from 'next/link'

export default function Header() {

    return (
        <div class="title-bar">
            <div class="title-bar-text"><Link href="/" style={{ color: 'white' }}>Notepadify</Link></div>
            <div class="title-bar-controls">
                <button aria-label="Minimize"></button>
                <button aria-label="Maximize"></button>
                <button aria-label="Close"></button>
            </div>
        </div>
    )
}