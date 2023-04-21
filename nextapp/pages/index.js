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
      <Chats />
      <div >
        {/* <div>
           <Sidebar>
            <ul className="bg-gray-900 rounded-lg my-8 p-3 ml-5 flex flex-col gap-4">
              <li  onClick={() => handleSidebarLinkClick("/")}>
                <a className="text-gray-300 hover:text-gray-200 cursor-pointer">Chat</a>
              </li>
              <li onClick={() => handleSidebarLinkClick("/visualize")}>
                <a className="text-gray-300 hover:text-gray-200 cursor-pointer">Visualize</a>
              </li>
            </ul>
          </Sidebar> 
        </div> */}
        
        {/* <div>
          {router.pathname === "/" ? <Chats /> : null}
          {router.pathname === "/visualize" ? <Visualize /> : null}
        </div> */}
      </div>
    </>
  )
}
