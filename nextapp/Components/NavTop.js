import React from 'react'
import styles from '../styles/Home.module.css'
function NavTop() {
  return (
    <div className={styles.topnav}>
        <div className = {styles.navlogo}>
          <a href="/">VirtualSenpai</a>
        </div>
        <div className = {styles.navlinks}>
          <a href="https://elfin-fireman-b6a.notion.site/Boctor-Docs-3aac831e62a947289304c95c476b93f2" target="_blank">Docs</a>
          <a href="https://github.com/BitNaysh/Boctor" target="_blank">GitHub</a>
        </div>       
      </div>
  )
}

export default NavTop