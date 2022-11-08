export default function Header() {

    return (
        <div class="window w-100">
            <div class="title-bar">
                <div class="title-bar-text">Notepadify</div>
                <div class="title-bar-controls">
                    <button aria-label="Minimize"></button>
                    <button aria-label="Maximize"></button>
                    <button aria-label="Close"></button>
                </div>
            </div>
            <div class="window-body">
                <div class="field-row">
                    <label for="title">Title</label>
                    <input type="text" name="title" id="title" />
                </div>
                <div class="field-row">
                    <label for="content">Content</label>
                    <textarea name="content" id="content" rows="3"></textarea>
                </div>
                <div class="field-row">
                    <button>Save</button>
                </div>
            </div>
        </div>
    )
}