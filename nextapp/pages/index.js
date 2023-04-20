import Head from "next/head"
import Chats from "./chats"
import Sidebar from "./Sidebar"
import NavTop from "./NavTop"

export default function Home() {

  

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
          <Sidebar />
        </div>
        <div>
          <Chats />
        </div>
      </div>
      
      
      
    </>
  )
}
