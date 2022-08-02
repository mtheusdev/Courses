import './styles.css';
import { useEffect, useState } from 'react'
import { loadPosts } from '../../utils/load-posts';
import { Posts } from '../../components/Posts';
import { Button } from '../../components/Button';
import { TextInput } from '../../components/TextInput';

export const Home = () => {

  const [posts, setPosts] = useState([])
  const [allPosts, setAllPosts] = useState([])
  const [page, setPage] = useState([])
  const [postsPerPage] = useState([])
  const [searchValue, setSearchValue] = useState([])

  const noMorePosts = page + postsPerPage >= allPosts.length
  const filteredPosts = !!searchValue ?
  
  allPosts.filter(post => {
    return post.title.toLowerCase().includes(searchValue.toLowerCase());
  })
  : posts

  const handleLoadPosts = async () => {
    const { page, postsPerPage } = this.state
    const postAndPhotos = await loadPosts()
    setPosts(postAndPhotos.slice(page, postsPerPage));
    setAllPosts(postAndPhotos)
  }

  const handleChange = (e) => {
    const { value } = e.target
    setSearchValue(value)
  }

  const loadMorePosts = () => {
    const nextPage = page + postsPerPage
    const nextPosts = allPosts.slice(nextPage, nextPage + postsPerPage)
    posts.push(...nextPosts)
    setPosts(posts)
    setPage(nextPage)
  }
  
  useEffect(() => {
    
  }, [])
  return (
    <section className="container">
      <div className="search-container">
        {!!searchValue && (
            <h1>Search Value: {searchValue}</h1>
        )}
        <TextInput searchValue={searchValue} handleChange={handleChange}/>
      </div>
      {filteredPosts.length > 0 && (
         <Posts posts={filteredPosts}/>
      )}
      {filteredPosts.length === 0 && (
         <p>Não existem posts</p>
      )}
      <div className="button-container">
      {!searchValue && (
        <Button text="load more posts"
          loadMoreClick={loadMorePosts}
          disabled={noMorePosts}
        />
        )
      }
      </div>  
    </section>
  );
}
// export class Home2 extends Component {
//   state = {
//     posts: [],
//     allPosts: [],
//     page: 0,
//     postsPerPage: 5,
//     searchValue: ''
//   }

//   async componentDidMount () {
//     await this.loadPosts()
//   }

//   loadPosts = async () => {
//     const { page, postsPerPage } = this.state
//     const postAndPhotos = await loadPosts()
//     this.setState({posts: postAndPhotos.slice(page, postsPerPage), allPosts:postAndPhotos})
//   }

//   handleChange = (e) => {
//     const { value } = e.target
//     this.setState({searchValue: value})

//   }

//   loadMorePosts = () => {
//     const {
//       page,
//       postsPerPage,
//       allPosts,
//       posts
//     } = this.state
//     const nextPage = page + postsPerPage
//     const nextPosts = allPosts.slice(nextPage, nextPage + postsPerPage)
//     posts.push(...nextPosts)
//     this.setState({posts, page: nextPage})
//   }

//   render(){
//     const {searchValue, posts, page, postsPerPage, allPosts} = this.state
//     const noMorePosts = page + postsPerPage >= allPosts.length
//     const filteredPosts = !!searchValue ?
//     allPosts.filter(post => {
//         return post.title.toLowerCase().includes(searchValue.toLowerCase());
//       })
//       : posts
//     return (
//       <section className="container">
//         <div className="search-container">
//           {!!searchValue && (
//               <h1>Search Value: {searchValue}</h1>
//           )}
//           <TextInput searchValue={searchValue} handleChange={this.handleChange}/>
//         </div>
//         {filteredPosts.length > 0 && (
//            <Posts posts={filteredPosts}/>
//         )}
//         {filteredPosts.length === 0 && (
//            <p>Não existem posts</p>
//         )}
//         <div className="button-container">
//         {!searchValue && (
//           <Button text="load more posts"
//             loadMoreClick={this.loadMorePosts}
//             disabled={noMorePosts}
//           />
//           )
//         }
//         </div>  
//       </section>
//     );
//   }
  
//}
