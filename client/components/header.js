export default function Header() {

    return (
        <div class="window main-container">
            <div class="title-bar">
                <div class="title-bar-text">Notepadify</div>
                <div class="title-bar-controls">
                    <button aria-label="Minimize"></button>
                    <button aria-label="Maximize"></button>
                    <button aria-label="Close"></button>
                </div>
            </div>
            <div id="content-body">
                {/* <div class="test"> */}
                {/* </div> */}
                {/* <div class="field-row">
                    <label for="title">Title</label>
                    <input type="text" name="title" id="title" />
                </div> */}
                {/* <label for="content">Content</label> */}
                <textarea name="content" id="content"></textarea>
            </div>
            <div class="footer">
                <button id="save-btn">Save</button>
            </div>
        </div>
    )
}