import Head from "next/head"
import Link from "next/link"
import { useRouter } from "next/router"
import Chats from "./chats"
import Visualize from "./visualize"
import Sidebar from "../Components/Sidebar"
import NavTop from "../Components/NavTop"

export default function Home() {
  const router = useRouter()

  const handleSidebarLinkClick = (route) => {
    router.push(route)
  }

  return (
    <>
      <Head>
        <title>Assist</title>
        <meta name="description" content="AI doctor chatbot" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <NavTop />
      <div className="flex">
        <div>
          <Sidebar>
            <ul>
              <li onClick={() => handleSidebarLinkClick("/")}>
                <a>Chat</a>
              </li>
              <li onClick={() => handleSidebarLinkClick("/visualize")}>
                <a>Visualize</a>
              </li>
            </ul>
          </Sidebar>
        </div>
        <div>
          {router.pathname === "/" ? <Chats /> : null}
          {router.pathname === "/visualize" ? <Visualize /> : null}
        </div>
      </div>
    </>
  )
}
