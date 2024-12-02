--
-- PostgreSQL database dump
--

-- Dumped from database version 17.2
-- Dumped by pg_dump version 17.2

-- Started on 2024-11-29 12:46:10

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 7 (class 2615 OID 16488)
-- Name: SSH2; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA "SSH2";


ALTER SCHEMA "SSH2" OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 226 (class 1259 OID 16490)
-- Name: ingredients; Type: TABLE; Schema: SSH2; Owner: postgres
--

CREATE TABLE "SSH2".ingredients (
    ingredient_id integer NOT NULL,
    ingredient_name text NOT NULL
);


ALTER TABLE "SSH2".ingredients OWNER TO postgres;

--
-- TOC entry 225 (class 1259 OID 16489)
-- Name: ingredients_ingredient_id_seq; Type: SEQUENCE; Schema: SSH2; Owner: postgres
--

ALTER TABLE "SSH2".ingredients ALTER COLUMN ingredient_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME "SSH2".ingredients_ingredient_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 229 (class 1259 OID 16505)
-- Name: linking; Type: TABLE; Schema: SSH2; Owner: postgres
--

CREATE TABLE "SSH2".linking (
    recipe_id integer NOT NULL,
    ingredient_id integer NOT NULL
);


ALTER TABLE "SSH2".linking OWNER TO postgres;

--
-- TOC entry 228 (class 1259 OID 16498)
-- Name: recipes; Type: TABLE; Schema: SSH2; Owner: postgres
--

CREATE TABLE "SSH2".recipes (
    recipe_id integer NOT NULL,
    recipe_name text NOT NULL,
    description text,
    prep_time time without time zone NOT NULL,
    cook_time time without time zone,
    servings integer NOT NULL,
    kcal integer NOT NULL,
    protein integer NOT NULL,
    "carbs(sugar)" text NOT NULL,
    "fat(saturates)" text NOT NULL,
    fibre integer NOT NULL,
    salt integer NOT NULL,
    instructions text NOT NULL
);


ALTER TABLE "SSH2".recipes OWNER TO postgres;

--
-- TOC entry 227 (class 1259 OID 16497)
-- Name: recipes_recipe_id_seq; Type: SEQUENCE; Schema: SSH2; Owner: postgres
--

ALTER TABLE "SSH2".recipes ALTER COLUMN recipe_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME "SSH2".recipes_recipe_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 4872 (class 0 OID 16490)
-- Dependencies: 226
-- Data for Name: ingredients; Type: TABLE DATA; Schema: SSH2; Owner: postgres
--

COPY "SSH2".ingredients (ingredient_id, ingredient_name) FROM stdin;
1	bay leaves
2	almond butter
3	baking powder
4	bananas
5	rosemary
6	gelatin
7	tofu
8	mustard
9	avocado oil
10	cumin
11	cinnamon
12	almonds
13	sage
14	pumpkin
15	vinegar
16	spinach
17	apples
18	sunflower oil
19	pickles
20	milk
21	baking soda
22	polenta
23	mint
24	gouda
25	cornstarch
26	cucumber
27	tahini
28	lime
29	vegetable oil
30	pineapple
31	lettuce
32	brown sugar
33	sesame oil
34	paprika
35	peanuts
36	oats
37	tomatoes
38	dill
39	dates
40	leeks
41	fish
42	pesto
43	parsley
44	cheese
45	shrimp
46	strawberries
47	garlic
48	barley
49	jam
50	pork
51	blueberries
52	cheddar cheese
53	guacamole
54	carrots
55	coconut
56	chives
57	goat cheese
58	mascarpone
59	brussels sprouts
60	potatoes
61	anise
62	cloves
63	sweet corn
64	asparagus
65	beets
66	pasta sauce
67	chocolate chips
68	coriander
69	rice
70	millet
71	basil
72	maple syrup
73	peas
74	honey
75	evaporated milk
76	bread
77	chili sauce
78	couscous
79	canola oil
80	pasta
81	soy sauce
82	yeast
83	powdered sugar
84	provolone
85	flour
86	whipping cream
87	zucchini
88	ricotta
89	sauerkraut
90	radishes
91	cream cheese
92	chili powder
93	eggplant
94	vanilla beans
95	black pepper
96	cream
97	tomato sauce
98	molasses
99	chili peppers
100	parmesan cheese
101	white pepper
102	cauliflower
103	ginger
104	coconut oil
105	hummus
106	icing sugar
107	nutmeg
108	squash
109	lentils
110	mayonnaise
111	olive oil
112	quinoa
113	chickpeas
114	fennel
115	ketchup
116	peanut butter
117	onions
118	cardamom
119	sugar
120	turmeric
121	mushrooms
122	green beans
123	miso
124	hot sauce
125	kimchi
126	oranges
127	eggs
128	lemon
129	peppers
130	granulated sugar
131	feta cheese
132	oregano
133	yogurt
134	farro
135	salt
136	thyme
137	vanilla extract
138	broccoli
139	mozzarella cheese
140	watermelon
141	olives
142	salsa
143	seaweed
144	cashews
145	avocado
146	butter
147	beef
148	cocoa powder
149	celery
150	raisins
151	condensed milk
152	chicken
153	walnuts
154	artichokes
155	arugula
156	bamboo shoots
157	caper berries
158	cherries
159	grapefruit
160	kiwifruit
161	mango
162	papaya
163	peaches
164	plums
165	pomegranate
166	rhubarb
167	snow peas
168	turnips
169	watercress
170	acorn squash
171	butternut squash
172	pecans
173	hazelnuts
174	macadamia nuts
175	quail eggs
176	duck eggs
177	prawns
178	scallops
179	lobster
180	clams
181	oysters
182	mussels
183	crab meat
184	anchovies
185	sardines
186	salmon
187	tuna
188	swordfish
189	tilapia
190	halibut
191	mahi mahi
192	trout
193	venison
194	duck meat
195	lamb
196	rabbit meat
197	turkey
198	bison
199	goose
200	kale
201	swiss chard
202	collard greens
203	okra
204	jalapeño peppers
205	habanero peppers
206	ghost peppers
207	shallots
208	fennel bulb
209	radicchio
210	endive
211	bok choy
212	savoy cabbage
213	daikon radish
214	ginger root
215	galangal
216	tamarind
217	kaffir lime leaves
218	lemongrass
219	water chestnuts
220	lotus root
221	seaweed nori
222	dried shiitake mushrooms
223	truffle oil
224	caviar
225	edamame
226	wasabi
227	mochi
228	miso paste
229	rice noodles
230	glass noodles
231	udon
232	soba noodles
233	ravioli
234	gnocchi
235	risotto
236	arborio rice
237	jasmine rice
238	basmati rice
239	wild rice
240	freekeh
241	spelt
242	teff
243	wheat bran
244	flaxseeds
245	chia seeds
246	hemp seeds
247	sunflower seeds
248	pumpkin seeds
249	sesame seeds
250	poppy seeds
251	quark cheese
252	pancetta
253	pecorino cheese
254	spaghetti
255	spice paste
256	greek yoghurt
257	spring onion
258	courgette
259	mangetout
260	hoisin sauce
261	beef mince
262	beef stock
263	coriander seeds
264	chilli flakes
265	corn flour
266	chocolate
267	white wine vinegar
\.


--
-- TOC entry 4875 (class 0 OID 16505)
-- Dependencies: 229
-- Data for Name: linking; Type: TABLE DATA; Schema: SSH2; Owner: postgres
--

COPY "SSH2".linking (recipe_id, ingredient_id) FROM stdin;
1	100
1	127
1	47
1	146
1	135
1	95
1	252
1	253
1	254
2	12
2	18
2	47
2	68
2	103
2	117
2	152
2	255
3	18
3	47
3	63
3	81
3	103
3	129
3	257
3	258
3	259
3	260
4	10
4	18
4	28
4	34
4	37
4	47
4	95
4	117
4	131
4	132
4	145
4	261
4	262
4	263
4	264
4	265
5	3
5	20
5	85
5	106
5	119
5	127
5	137
5	146
5	148
5	266
6	31
6	47
6	100
6	110
6	111
6	152
6	184
6	267
\.


--
-- TOC entry 4874 (class 0 OID 16498)
-- Dependencies: 228
-- Data for Name: recipes; Type: TABLE DATA; Schema: SSH2; Owner: postgres
--

COPY "SSH2".recipes (recipe_id, recipe_name, description, prep_time, cook_time, servings, kcal, protein, "carbs(sugar)", "fat(saturates)", fibre, salt, instructions) FROM stdin;
1	Spaghetti Carbonara	Classic Italian pasta with a creamy sauce.	00:10:00	00:20:00	2	400	15	40(5)	10(3)	5	1	Cook pasta. Mix eggs and cheese. Combine with pasta and pancetta.
2	Chicken Curry	Spicy and flavorful chicken dish.	00:15:00	00:30:00	4	500	30	50(8)	15(4)	7	2	Cook chicken with spices. Add coconut milk and simmer. Serve with rice.
3	Vegetable Stir Fry	Quick and healthy stir-fried vegetables.	00:10:00	00:15:00	2	300	10	30(4)	5(1)	6	1	Stir-fry vegetables with soy sauce and garlic. Serve with noodles or rice.
4	Beef Tacos	Mexican tacos with seasoned beef.	00:15:00	00:20:00	4	450	25	35(6)	20(7)	4	2	Cook beef with spices. Assemble tacos with toppings.
5	Chocolate Cake	Rich and moist chocolate dessert.	00:20:00	00:40:00	8	600	5	50(25)	25(10)	3	1	Mix ingredients, bake in oven, and let cool before serving.
6	Caesar Salad	Crisp romaine lettuce with creamy Caesar dressing.	00:10:00	00:20:00	2	250	10	20(2)	10(3)	3	1	Chop lettuce and toss with dressing. Add croutons and cheese.
7	Grilled Cheese Sandwich	Crispy grilled sandwich with melted cheese.	00:10:00	00:20:00	1	400	15	30(4)	15(6)	2	2	Butter bread, add cheese, and grill until golden.
8	Tomato Soup	Warm tomato soup with herbs and spices.	00:10:00	00:20:00	2	200	5	15(2)	5(1)	3	1	Cook tomatoes with spices, blend, and serve hot.
9	Fried Rice	Fried rice with vegetables and soy sauce.	00:10:00	00:20:00	4	300	8	40(5)	15(4)	5	2	Stir-fry rice with vegetables, soy sauce, and garlic.
10	Pan-Seared Salmon	Seared salmon served with lemon butter sauce.	00:10:00	00:20:00	2	500	40	5(0)	20(7)	2	1	Pan-sear salmon with seasoning and serve with sauce.
11	Margherita Pizza	Classic pizza with tomato, basil, and mozzarella.	00:10:00	00:20:00	4	400	15	50(6)	10(3)	4	1	Spread tomato sauce, add cheese and bake pizza.
12	Stuffed Bell Peppers	Bell peppers stuffed with rice and ground meat.	00:10:00	00:20:00	4	350	20	30(4)	10(3)	5	2	Fill bell peppers with mixture, bake, and serve.
14	Vegetable Curry	Spicy vegetable curry served with rice or naan.	00:10:00	00:20:00	4	450	15	45(6)	10(3)	6	1	Cook vegetables with spices and serve with rice.
15	Shrimp Scampi	Juicy shrimp cooked in garlic butter sauce.	00:10:00	00:20:00	2	550	30	10(1)	20(6)	2	1	Cook shrimp in garlic butter and serve with pasta.
16	Chicken Alfredo	Creamy Alfredo pasta with grilled chicken.	00:10:00	00:20:00	4	700	40	50(8)	20(7)	4	2	Cook pasta and mix with creamy Alfredo sauce.
17	Beef Stroganoff	Hearty beef pasta dish with creamy sauce.	00:10:00	00:20:00	4	650	35	50(7)	20(6)	4	2	Cook beef with sauce and serve with pasta.
18	Pulled Pork Sandwich	Slow-cooked pork served in a sandwich bun.	00:10:00	00:20:00	2	500	20	40(6)	25(10)	3	2	Slow-cook pork and assemble in sandwich buns.
19	Lasagna	Layers of pasta, cheese, and meat sauce.	00:10:00	00:20:00	6	800	25	60(8)	25(10)	5	2	Layer pasta, meat sauce, and cheese, then bake.
20	Eggplant Parmesan	Baked eggplant with marinara sauce and cheese.	00:10:00	00:20:00	4	450	15	30(4)	10(3)	4	1	Bake eggplant with marinara sauce and cheese.
21	Roast Chicken	Juicy roast chicken with herbs and spices.	00:10:00	00:20:00	4	600	35	20(2)	20(6)	3	2	Roast chicken with herbs and serve hot.
22	Potato Wedges	Crispy potato wedges seasoned with herbs.	00:10:00	00:20:00	4	300	8	40(4)	15(4)	5	1	Cut potatoes, season, and bake until crispy.
23	Pancakes	Fluffy pancakes served with syrup and butter.	00:10:00	00:20:00	4	400	10	50(8)	15(6)	3	1	Mix batter and cook pancakes. Serve with syrup.
24	Waffles	Crispy waffles with fruit and whipped cream.	00:10:00	00:20:00	4	400	10	50(7)	20(7)	4	1	Mix batter and cook waffles. Add toppings.
25	French Toast	Thick French toast dusted with powdered sugar.	00:10:00	00:20:00	4	350	8	30(4)	15(6)	3	1	Dip bread in egg mixture and cook. Add syrup.
26	Smoothie Bowl	Smoothie with fruit, granola, and seeds.	00:10:00	00:20:00	1	250	5	30(5)	5(2)	3	1	Blend fruits, pour into a bowl, and add toppings.
27	Quinoa Salad	Healthy salad with quinoa and fresh vegetables.	00:10:00	00:20:00	2	350	10	35(6)	10(3)	5	1	Mix quinoa, vegetables, and dressing. Serve fresh.
28	Greek Salad	Greek-style salad with feta cheese and olives.	00:10:00	00:20:00	4	300	8	30(5)	8(2)	4	1	Chop vegetables and toss with olives and feta.
29	Minestrone Soup	Hearty vegetable soup with pasta.	00:10:00	00:20:00	6	200	7	20(4)	5(2)	6	1	Cook vegetables with pasta in broth. Serve hot.
30	Clam Chowder	Creamy clam chowder with potatoes and celery.	00:10:00	00:20:00	4	400	10	20(4)	20(7)	4	2	Cook clams with cream and serve warm.
31	Cabbage Rolls	Cabbage leaves stuffed with rice and meat.	00:10:00	00:20:00	4	400	20	30(4)	15(6)	4	2	Stuff cabbage leaves with meat and rice, then bake.
32	Meatballs	Juicy meatballs in marinara sauce.	00:10:00	00:20:00	4	500	30	20(3)	25(10)	4	2	Cook meatballs in sauce and serve with pasta.
33	Baked Ziti	Baked pasta with cheese and tomato sauce.	00:10:00	00:20:00	4	600	20	40(5)	25(10)	4	1	Mix pasta, sauce, and cheese. Bake until golden.
34	Pumpkin Soup	Warm pumpkin soup spiced with nutmeg.	00:10:00	00:20:00	4	300	5	20(4)	5(2)	3	1	Cook pumpkin, blend, and add spices for soup.
35	Apple Pie	Classic dessert with spiced apples in a crust.	00:10:00	00:20:00	6	450	5	40(5)	15(6)	3	1	Prepare apple filling, assemble, and bake pie.
13	Shepards Pie	Traditional dish with ground meat and mashed potatoes.	00:10:00	00:20:00	6	600	25	40(5)	15(6)	6	2	Cook meat, layer with potatoes, and bake.
\.


--
-- TOC entry 4881 (class 0 OID 0)
-- Dependencies: 225
-- Name: ingredients_ingredient_id_seq; Type: SEQUENCE SET; Schema: SSH2; Owner: postgres
--

SELECT pg_catalog.setval('"SSH2".ingredients_ingredient_id_seq', 267, true);


--
-- TOC entry 4882 (class 0 OID 0)
-- Dependencies: 227
-- Name: recipes_recipe_id_seq; Type: SEQUENCE SET; Schema: SSH2; Owner: postgres
--

SELECT pg_catalog.setval('"SSH2".recipes_recipe_id_seq', 1, false);


--
-- TOC entry 4721 (class 2606 OID 16496)
-- Name: ingredients ingredients_pkey; Type: CONSTRAINT; Schema: SSH2; Owner: postgres
--

ALTER TABLE ONLY "SSH2".ingredients
    ADD CONSTRAINT ingredients_pkey PRIMARY KEY (ingredient_id);


--
-- TOC entry 4723 (class 2606 OID 16504)
-- Name: recipes recipes_pkey; Type: CONSTRAINT; Schema: SSH2; Owner: postgres
--

ALTER TABLE ONLY "SSH2".recipes
    ADD CONSTRAINT recipes_pkey PRIMARY KEY (recipe_id);


--
-- TOC entry 4724 (class 2606 OID 16513)
-- Name: linking ingredient_id; Type: FK CONSTRAINT; Schema: SSH2; Owner: postgres
--

ALTER TABLE ONLY "SSH2".linking
    ADD CONSTRAINT ingredient_id FOREIGN KEY (ingredient_id) REFERENCES "SSH2".ingredients(ingredient_id) NOT VALID;


--
-- TOC entry 4725 (class 2606 OID 16508)
-- Name: linking recipe_id; Type: FK CONSTRAINT; Schema: SSH2; Owner: postgres
--

ALTER TABLE ONLY "SSH2".linking
    ADD CONSTRAINT recipe_id FOREIGN KEY (recipe_id) REFERENCES "SSH2".recipes(recipe_id) NOT VALID;


-- Completed on 2024-11-29 12:46:11

--
-- PostgreSQL database dump complete
--

