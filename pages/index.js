export default function Home() {
  return (
    <div>
      <h1>Welcome to {process.env.NEXT_PUBLIC_AUTHOR_NAME}'s Blog</h1>
      <p>This is my personal blog where I share my thoughts and experiences.</p>
    </div>
  )
}