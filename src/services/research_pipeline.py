from src.services import create_search_llm, create_reader_llm
from src.chains import writer_chain, critic_chain

def run_research_pipeline(topic: str) -> dict:
     state = {}

     print('\n', '='*50)
     print("Step 1 - Search agent is working...")
     
     search_llm = create_search_llm()

     search_result = search_llm.invoke({
          'messages' : [("user", f"Find recent, reliable and detailed information about: {topic}")]
     })

     state['search_results'] = str(search_result['messages'][-1].content)
     print("Search Result:\n", state['search_results'])

     print('\n', '='*50)
     print("Step 2 - Reader agent is scraping top resources...")

     reader_llm = create_reader_llm()

     reader_result = reader_llm.invoke({
         "messages": [("user", 
             f"Based on the following search results about '{topic}', "
             f"pick the most relevant URL and scrape it for deeper content.\n\n"
             f"Search Results:\n{state['search_results'][:800]}"
         )]
     })
     
     scraped_raw = reader_result['messages'][-1].content
     
     if isinstance(scraped_raw, list):
         state['scraped_content'] = "".join([item.get('text', '') for item in scraped_raw if isinstance(item, dict)])
     else:
  
         state['scraped_content'] = str(scraped_raw)
         
     print("Scraped Content:\n", state['scraped_content'])

     print('\n', '='*50)
     print("Step 3 - Writer is drafting the report...")

     ressearch_combined = (
          f"SEARCH RESULT: \n {state['search_results']}\n\n"
          f"DETAILED SCRAPED CONTENT: \n {state['scraped_content']}\n\n"
     )

     state['report'] = str(writer_chain.invoke(
          {"topic" : topic,
           "research" : ressearch_combined}
     ))

     print('\n', '='*50)
     print("Final report...\n", state['report']) 

     print('\n', '='*50)
     print("Step 4 - Critic reviewing the report...")

     state['feedback'] = str(critic_chain.invoke({
          "report" : state['report']
     }))

     print("\n critic report \n", state['feedback'])

     return state