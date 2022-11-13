import { useRouter } from 'next/router'

export default function Footer(props) {
    const { push } = useRouter();
    function on_save_click() {
        props.onClick()
        .then((pk) => {
            push(`/${pk}`)
        })
    }
    
    return (
        <div class="footer">
            <button id="save-btn" onClick={ () => on_save_click(props.onClick) }>Save</button>
        </div>
    )
}