import Header from "./header";


export default function Base({ children }) {
    return (
        <>
            <Header />
            {children}
        </>
    )
}