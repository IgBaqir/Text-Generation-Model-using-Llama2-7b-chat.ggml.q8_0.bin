import streamlit as st 
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers

## function to get response from my Llama 2 model
def getLlamareponse(input_text, no_words, blog_style):
    
    ## LLAma2 model
    llm = CTransformers(model='/Users/baqir/Projects (Jupyter)/Blog Llama2/Model/llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type ='llama',
                        config = {'max_new_tokens': 256,
                                  'temperature':0.01})
    ## prompt template
    
    template = """
    write a blog for {blog_style} job profile for a topic {input_text} 
    within {no_words} words.
      """
    
    prompt = PromptTemplate(input_variables=["blog_style","input_text","no_words"],template=template)
    
    ## generate the reponse from the llama 2 model
   
    response = llm.invoke(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
    print(response)
    return response






st.set_page_config( page_title = "Generate Blogs",
                       page_icon='®',
                       layout ='centered',
                       initial_sidebar_state ='collapsed')

st.header("Generate Blogs")

input_text = st.text_input("Enter the blog topic")

## creating 2 more columns for additional 2 fields

col1, col2 = st.columns([5,5])

with col1:
    no_words = st.text_input('No. of words')
with col2:
    blog_style=st.selectbox('Writing the blog for ',
                            ('researchers','Data scientists','Common people'),index=0)

submit=st.button("Generate")    

## Final response

if submit:
    if input_text.strip() and no_words.strip() and blog_style:
        response = getLlamareponse(input_text, no_words, blog_style)
        st.write(response)
    else:
        st.error("Please fill in all the fields correctly.")
