
// Names of components must be written using capital letter.
function NavBarComponent(prop) {
    return (

    <nav id="bootstrap-overrides-navbar" className="navbar navbar-expand-md navbar-dark" aria-label="Fourth navbar example">
        <div className="container-fluid">
            <a id="bootstrap-overrides-logo" className="navbar-brand px-3" href="#">ggoj_beauty</a>
            <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarsExample04" aria-controls="navbarsExample04" aria-expanded="false" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
            </button>

            <div className="collapse navbar-collapse" id="navbarsExample04">
                <ul className="navbar-nav me-auto mb-2 mb-md-0">
                <li className="nav-item">
                    <a className="nav-link active" aria-current="page" href="#">O mnie</a>
                </li>
                <li className="nav-item">
                    <a className="nav-link" href="#">Cennik</a>
                </li>
                <li className="nav-item">
                    <a className="nav-link" href="#">Usługi</a>
                </li>
                <li className="nav-item">
                    <a className="nav-link">Blog</a>
                </li>
                <li className="nav-item">
                    <a className="nav-link" href="#">Kontakt</a>
                </li>
                </ul>
                {/* <form role="search">
                <input className="form-control" type="search" placeholder="Search" aria-label="Search" spellcheck="false" data-ms-editor="true">
                </form> */}
            </div>
        </div>
    </nav>
    );
}

export default NavBarComponent;