import Header from "./header";


export default function Base({ children }) {
    return (
        <div class="main-container">
        
            <Header />
            {children}
        </div>
    )
}