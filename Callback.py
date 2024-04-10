class Callback:
    @staticmethod
    def master_callback(paper):
        Callback.print_paper(paper)
        Callback.counter(paper)

    @staticmethod
    def print_paper(paper):
        print("Author:", paper.author if paper.author else "None")
        try:
            title = paper.title.encode('utf-8', errors='ignore').decode('utf-8', errors='ignore')
            print("Title:", title if title else "None")
        except UnicodeEncodeError:
            print("Title: [Unable to display due to encoding error]")
        print("Paper ID:", paper.paper_id if paper.paper_id else "None")
        print("Year:", paper.year if paper.year else "None")
        print("Pages:", paper.pages if paper.pages else "None")
        print("URL:", paper.url if paper.url else "None")
        print("DOI:", paper.doi if paper.doi else "None")
        print("Published through:", paper.published_through if paper.published_through else "None")
        print("----------------------------")

    @staticmethod
    def counter(paper):
        if paper.file_source == "DBLP":
            Callback.dblp_title_counter += 1
            Callback.dblp_title_char_counter += len(paper.title) if paper.title else 0
        elif paper.file_source == "MAG":
            Callback.mag_title_counter += 1
            Callback.mag_title_char_counter += len(paper.title) if paper.title else 0

# Initialize global counters
Callback.dblp_title_counter = 0
Callback.mag_title_counter = 0
Callback.dblp_title_char_counter = 0
Callback.mag_title_char_counter = 0
