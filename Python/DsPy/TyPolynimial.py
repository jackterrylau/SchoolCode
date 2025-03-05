#import DsLinkedList
from typing import Union #Py: Python 的 Union[type1,type2,...] = type1 | type2 | ...
from enum import Enum
import copy

class PolyNodeType(Enum):
    POLY = 1
    ATOM = 2
    SUBLIST = 3

class PolyNode:
    """ This is a Generalized Node of Polynomial supporting multiple Variables. """

    def __init__(self, NodeType=PolyNodeType.POLY, var=None, exp=0, data=1.0, parent=None, pnode=None, next=None):

        #self.data: Union[str, float, PolyNode] #Py: Assign union type to data
        self._NodeType = NodeType
        self._Var = var
        self.Coef = 0.0
        self.Sub = None
        self.Exp = exp
        self._PNode = pnode
        self._Next = next

        self._outVarItems = []
        self._Parent = parent
       
        if NodeType == PolyNodeType.POLY:
            if isinstance(data, str): 
                self._Var = data
                self.Coef = None
                self.Sub = None
                self.Exp = None
                if isinstance(parent, PolyNode): 
                    self._outVarItems = copy.deepcopy(parent.PNode._outVarItems) if parent else []
                    self._outVarItems.insert(0, {"outVar":parent.PNode.Var, "outExp":parent.Exp})

            else: raise Exception("[Invalid Parameters] the NodeType should be matched with data for Polynomial Node")
        elif NodeType == PolyNodeType.ATOM:
            if isinstance(data, float): 
                self._Var = self.PNode.Var if self._PNode else None
                self.Coef = data; self.Sub = None
                self._outVarItems = self.PNode._outVarItems if self._PNode else []
            else: raise Exception("[Invalid Parameters] the NodeType should be matched with data for Polynomial Node")
        elif NodeType == PolyNodeType.SUBLIST:
            if not data: self.Sub = None
            elif isinstance(data, PolyNode): 
                if data.NodeType == NodeType.POLY: 
                    self.Sub = data
                    self._outVarItems = self.PNode._outVarItems if self._PNode else []
                else: raise Exception("[Invalid Parameters] the NodeType of Sub List should be NodeType.POLY")
            else: raise Exception("[Invalid Parameters] the NodeType should be matched with data for Polynomial Node")
        else: raise Exception("[Invalid Parameters] the NodeType is invalid")

    @property
    def NodeType(self): return self._NodeType

    @property
    def Var(self): return self._Var
    @Var.setter
    def Var(self, value): self._Var = value

    @property
    def Parent(self): return self._Parent
    @Parent.setter
    def Parent(self, value): 
        if self._NodeType != PolyNodeType.POLY: raise Exception("[Invalid Value] Only PolyNodeType.POLY node can have a parent sublist node")
        if isinstance(value, PolyNode): 
            self._Parent = value
            self._outVarItems.insert(0, {"outVar":value.PNode.Var, "outExp":value.Exp})
            #DEBUG: print(f"Initial[1-0] NewNode={self}, NewNode.Var={self._Var},       self._Parent={self._Parent}")
            #DEBUG: print(f"Initial[1-1] self._outVarItems={self._outVarItems}")
        else: Exception("[Invalid Value] the type of 'parent' value should be a Polynomial Node")

    @property
    def Next(self): return self._Next
    @Next.setter
    def Next(self, value): 
        if isinstance(value, PolyNode) or (not value): self._Next = value; return True
        raise Exception("[Invalid Value] the type of 'next' value should be a Polynomial Node")
    
    @property
    def PNode(self): return self._PNode
    @PNode.setter
    def PNode(self, value): 
        if self._NodeType == PolyNodeType.POLY: raise Exception("[Invalid Value] PolyNodeType.POLY Node can't setup PNode")
        if isinstance(value, PolyNode): 
            if value.NodeType != PolyNodeType.POLY: 
                raise Exception("[Invalid Value] the NodeType of 'PNode' should be PolyNodeType.POLY")
            self._PNode = value

            if self._NodeType == PolyNodeType.ATOM:
                self._outVarItems = value._outVarItems
            return True
        raise Exception("[Invalid Value] the type of 'PNode' value should be a Polynomial Node")
    
    def to_poly_item(self, is_readable=False):
        if self._NodeType != PolyNodeType.ATOM: raise Exception("[Invalid Value] Only ATOM Node can be to a polyminal item.")
        s = f"+{self.Coef}" if self.Coef >= 0.0 else self.Coef
        poly_item = str(s) + self._Var 
        if is_readable:
            poly_item = poly_item if self.Exp != 0 else str(s)
            if self.Exp in [0,1]: return poly_item+self.getOutVarItemsStr(is_readable)
            else: return poly_item+digits_to_sup(self.Exp)+self.getOutVarItemsStr(is_readable)
        poly_item += digits_to_sup(self.Exp)+self.getOutVarItemsStr()

        return poly_item
    
    def getOutVarItemsStr(self, is_readable=False):
        outVarsStr = ""
        
        for i in range(len(self._outVarItems)):
            #DEBUG: print(f"poly_item = {poly_item}; (o_var, o_exp) = {self._outVarItems[i]["outVar"], self._outVarItems[i]["outExp"]}")
            if (is_readable and self._outVarItems[i]["outExp"]==0): continue
            outVarsStr = outVarsStr + self._outVarItems[i]["outVar"]
            if self._outVarItems[i]["outExp"] != 1: outVarsStr += digits_to_sup(self._outVarItems[i]["outExp"])
        
        return outVarsStr
    
    def visit(self,n=None,visit_str="", backto=None):
        # 如果有子節點 則 拜訪(Print)
        # 子節點也執行自己的子節點拜訪程序
        # 直到沒有子節點 則 Return
        node = n if n else self
        nodes = []      
        s = visit_str
        if node:
            visit_sign = ""
            #print(f"{node} - {node.NodeType} -> ")
            nodes.append(node)
            if node.NodeType == PolyNodeType.SUBLIST: 
                visit_sign = "S(" + str(node.Exp) + ")"
                backto = node.Next
                #print(f"%%%%%%%%%%%backto = {backto}")
                s += visit_sign + "==>"
                node = node.Sub
            else: 
                if node.NodeType == PolyNodeType.POLY: visit_sign = "P("+str(node.Var)+")"
                else: visit_sign = "A("+str(node.Coef) + str(node.Var) + "^" + str(node.Exp) + ")"
                s += visit_sign + "-->"
                node = node.Next
            if node: return node.visit(n,s,backto)
            else: 
                s += "NULL"
                if backto: 
                    s += "-->"
                    return backto.visit(visit_str=s)
        return s

    def __repr__(self):
        if self._NodeType == PolyNodeType.POLY: 
            return "<P>:{1}{0}".format(self._Var, self.getOutVarItemsStr())
        elif self._NodeType == PolyNodeType.ATOM: 
            return "<A>:{0}{1}{2}{3}".format(self.Coef, self._Var, digits_to_sup(self.Exp), self.getOutVarItemsStr())
        else:
            return "<S>:{0}{1}-{2}-->{3}".format(self._PNode.Var, digits_to_sup(self.Exp), self.Sub, self._Next)

def add_new_out_var_to_sub(node):
    """ 當有新的 sublist node 插入到多項式中, 後面在更新 多項式項的 Exp 時, 必須將該新插入的 node 的 PNnode.Var 加入到 sublist 底下的 PNnode 中
    """
    if node.PNode._outVarItems:
        n1_pn_out_vars = [ovi["outVar"] for ovi in node.PNode._outVarItems]
        n1_sub_out_vars = [ovi["outVar"] for ovi in node.Sub._outVarItems]
        newOutVars = list(set(n1_pn_out_vars).difference(set(n1_sub_out_vars)))
        newOutExp = 0
        for i in range(len(newOutVars)):
            for j in range(len(n1_sub_out_vars)):
                #DEBUG: print("i5i5i5i5i5i5    newOutVars[%s] = %s, n1_sub_out_vars[%s]= %s"%(i,newOutVars[i],j,n1_sub_out_vars[j]))
                if newOutVars[i] < n1_sub_out_vars[j]: continue
                else: 
                    for out_var_item in node.PNode._outVarItems:
                        if out_var_item["outVar"] == newOutVars[i]: newOutExp = out_var_item["outExp"]; break
                    add_new_out_var_to_branch_nodes(node.Sub, newOutVars[i], newOutExp)
        return True

def add_new_out_var_to_branch_nodes(node, new_var, new_var_exp, backto=None):
    """ 將新插入 PNnode 的 node Out Var 同步到 其 底下所有 node 中
    """   

    #DEBUG: print("iiiiiiiiii1    node = %s "%node)
    isNewOutVar = True
    node_out_vars = [ovi["outVar"] for ovi in node._outVarItems] if node else []
    for j in range(len(node_out_vars)):
        if new_var != node_out_vars[j]: continue
        else: isNewOutVar = False
        if j >= len(node_out_vars)-1 and isNewOutVar: isNewOutVar = False if new_var == node.Var else isNewOutVar

    if node:
        if node.NodeType == PolyNodeType.SUBLIST: 
            backto = node.Next
            node = node.Sub
        else: 
            for j in range(len(node_out_vars)):
                if new_var < node_out_vars[j]: continue
                else: 
                    if new_var == node_out_vars[j]: node._outVarItems[j]["outExp"] = new_var_exp
                    else: 
                        if isNewOutVar: 
                            node._outVarItems.insert(j+1, {"outVar":new_var,"outExp":new_var_exp})
            node = node.Next
        return add_new_out_var_to_branch_nodes(node, new_var, new_var_exp, backto)
    else: 
        if backto: return add_new_out_var_to_branch_nodes(node, new_var, new_var_exp, backto)
        else: return True

def multiplyPolynomial(pnodeStr1:str, pnodeStr2:str) -> PolyNode:
    """ 兩個多項式相乘後 產生新的結果多項式. 
    """

    PNode = None
    PNode1 = polyFormulaToNode(pnodeStr1); PItems1 = splitPolynomial(pnodeStr1); PItems2 = splitPolynomial(pnodeStr2)
    if len(PItems1) < len(PItems2):
        PNode1 = polyFormulaToNode(pnodeStr2); t=PItems1; PItems1=PItems2; PItems2=t
    back_sub_list = []
    new_big_nodes = []
    
    #Tips: PItems2 中所有每一項 都需要跟 被乘式 的每一項相乘
    for i in range(len(PItems2)):
        
        new_big_node = copy.deepcopy(PNode1)
        n1 = new_big_node

        #777. Tips: 先把所有 ATOM Node 的 Coef 乘上 PItems2 的 Coef
        m_coef = get_poly_item_coef_and_vars(PItems2[i])["coef"]
        while n1:
            if n1.NodeType == PolyNodeType.POLY:
                n1 = n1.Next
            elif n1.NodeType == PolyNodeType.ATOM:
                #Tips: 只要遇到 ATOM 就 將其 係數 乘上 被乘項 的 第 i 項 的 係數
                n1.Coef = n1.Coef * m_coef
                if not n1.Next and back_sub_list: n1 = back_sub_list.pop(0); continue
                n1 = n1.Next
            else:
                if n1.Next and n1.Next.NodeType == PolyNodeType.SUBLIST: 
                    back_sub_list.insert(0, n1.Next)
                n1 = n1.Sub
        #777. End
        #DEBUG: print("HHHHH Coef - new_big_node = %s HHHHH"%new_big_node.visit())

        #2832. Tips: 乘式項中有不存在於被乘式項的變數
        #DEBUG: print("get_poly_item_coef_and_vars.PItems1 = %s"%(PItems1))
        #DEBUG: print("get_poly_item_coef_and_vars.PItems2[%d] = %s"%(i, PItems2[i]))
        pNode1VarItems = get_poly_item_coef_and_vars(PItems1[0])["vars"]
        pnVarItems_keys = [pvitem["v"] for pvitem in pNode1VarItems] 
        PItems2VarItems = get_poly_item_coef_and_vars(PItems2[i])["vars"]
        PItems2VarItems_keys = [vitem["v"] for vitem in PItems2VarItems]

        #Python: PItems2VarItems 中有而 PItems1(pNode1VarItems) 中没有的 變數 需要插入到 PItems1
        newVarKeys = list(set(PItems2VarItems_keys).difference(set(pnVarItems_keys))) 
        #DEBUG: print("222 222 newVarKeys = %s"%(newVarKeys))

        while newVarKeys:
            t_node = new_big_node
            pre_t_node = None
            t_origin_sublist_node = None
            t_next_sublist_node = None
            t_pnx = None
            newVar = newVarKeys.pop(0)
            newExp = 0.0
            #25975. Tips: Setup newVar.Exp
            for vi in range(len(PItems2VarItems)):
                if PItems2VarItems[vi]["v"] == newVar: newExp = PItems2VarItems[vi]["e"]; break
            #25975. End

            #Tips: 取 PItems1 中 的變數 來與 newVar 比較
            comparedPnVar = pnVarItems_keys.pop(0)

            # Tips: PItems1 最大的變數 小於 乘式 中 的 項 的 最大變數, 把 乘式 中 的 變數插入到 new_big_node
            while t_node: 
                if newVar > comparedPnVar: 
                    #DEBUG: print("++++++ newVar > comparedPnVar : %s > %s"%(newVar, comparedPnVar))
                    if pre_t_node: 
                        if pre_t_node.NodeType != PolyNodeType.POLY: pre_t_node = pre_t_node.PNode
                    newVarNode = pnode_add_vars([newVar],t_node)
                    if pre_t_node: pre_t_node.Next.Sub = newVarNode
                    if pre_t_node: newVarNode.Parent = pre_t_node.Next
                    #DEBUG: print("++++++ new_big_node(newVar(%s)>comparedPnVar(%s)) : %s"%(newVar,comparedPnVar,new_big_node.visit()))
                    break
                # Tips: comparedPnVar 比 newVar 大的話, 則繼續往下找到適合插入 newVar 的位置
                elif newVar < comparedPnVar:
                    #DEBUG: print("newVar < comparedPnVar: t_node = %s, newVar = %s, comparedPnVar = %s "%(t_node, newVar, comparedPnVar))
                    if t_node.Next and t_node.Next.NodeType == PolyNodeType.SUBLIST:
                        #t_origin_sublist_node: 用來記錄目前正在拜訪但尚未拜訪完成的 sublist node, 將來 拜訪完時, 該 node 可以指定為 下一個將拜訪的 sublist node 的 pre_t_note
                        t_origin_sublist_node = t_node if t_node.NodeType == PolyNodeType.SUBLIST else t_node.Next
                        #pre_t_node: 更新為現在的 sublist node 
                        pre_t_node = t_node
                        #t_node: go to 現在 Poly node 的下一個 sublist node 下面的 POLY Node, NEXT Visiting NODE
                        t_node = t_node.Next.Sub 
                        #t_next_sublist_node: 現在的 sublist node 後面的 sublist node 或 NULL 
                        t_next_sublist_node = t_node.Next if (t_node.Next and t_node.Next.NodeType==PolyNodeType.SUBLIST) else None
                        comparedPnVar = t_node.Var
                        #DEBUG: print("newVar < comparedPnVar 1: pre_t_node = %s, t_node = %s, t_next_sublist_node = %s \
                        #    newVar = %s, comparedPnVar = %s " %(pre_t_node, t_node, t_next_sublist_node, newVar, comparedPnVar))
                    elif t_node.Next and t_node.Next.NodeType == PolyNodeType.POLY:
                        pre_t_node = t_node; t_node = t_node.Next
                        comparedPnVar = t_node.Var
                    elif t_node.Next and t_node.Next.NodeType == PolyNodeType.ATOM:
                        pre_t_node = t_node; t_node = t_node.Next
                    #Tips: newVar = comparedPnVar, 相同變數則直接運算

                    #3172. Tips: 當拜訪到最末端的節點
                    if not t_node.Next:
                        #Tips: 當上層 還有下一個 sublist node 尚未拜訪 則回到上層尚未拜訪的 sublist 節點繼續尋找可插入 newVar 的位置
                        if t_next_sublist_node:
                            pre_t_node = t_origin_sublist_node
                            t_node = t_next_sublist_node
                            #DEBUG: print("555 555 pre_t_node = %s, t_node = %s, newVar = %s, comparedPnVar = %s " %(pre_t_node, t_node, newVar, comparedPnVar))
                            continue
                        #Tips: 當上層 沒有下一個 sublist node 整個走訪已經到底, 直接插入 newVar
                        else: 
                            if t_node.NodeType == PolyNodeType.SUBLIST:
                                t_snx = PolyNode(PolyNodeType.SUBLIST, exp=newExp, data=t_node.Sub)
                                t_pnx = PolyNode(PolyNodeType.POLY, data=newVar, next=t_snx)
                                t_node.PNode.Next.Sub = t_pnx # ignore?
                                t_snx.PNode = t_pnx
                                t_snx.PNode = t_node.PNode
                            break
                    #3172. End
                else: 
                    if t_node.Next: t_node = t_node.Next if t_node.Next.NodeType == PolyNodeType.ATOM else t_node.Next.Sub; break
            #2832. End

            #771. Tips: 更新 所有變數 的 Exp 次方數
        t_PItems2VarItems = copy.deepcopy(PItems2VarItems)
        while PItems2VarItems:
            #Tips. p2_var: 當下乘式中要跟被乘式相乘的變數
            p2_var = PItems2VarItems.pop(0)
            #Tips: n1- Current Visiting Node in new_big_node poly item
            n1 = new_big_node
            back_sub_list = []
            while n1:
                if n1.NodeType == PolyNodeType.POLY: n1 = n1.Next; continue
                #DEBUG: print("AAAAAAA    n1= %s, type = %s    AAAAAAA"%(n1, n1.NodeType))
                elif n1.NodeType == PolyNodeType.ATOM:
                    if n1.PNode.Var == p2_var["v"]: n1.Exp = n1.Exp + p2_var["e"]

                    for n1_ovi in range(len(n1._outVarItems)):
                        for pn_ovi in range(len(n1.PNode._outVarItems)):
                            if n1._outVarItems[n1_ovi]["outVar"] == n1.PNode._outVarItems[pn_ovi]["outVar"]:
                                n1._outVarItems[n1_ovi]["outExp"] = n1.PNode._outVarItems[pn_ovi]["outExp"]
                                #DEBUG: print("GGGGGGG 2 update atom_n1_ovi= [%s] to pn_ovi = [%s]"%(n1.PNode._outVarItems[pn_ovi],n1._outVarItems[n1_ovi]))
                                break

                    if not n1.Next and back_sub_list: n1 = back_sub_list.pop(0); continue
                    n1 = n1.Next

                #Tips: SUBLIST
                else:
                    #DEBUG: print("GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG S.1 n1 = %s,    n1(S).PNode.Var=%s,    p2_var['v']=%s"%(n1,n1.PNode.Var,p2_var["v"]))
                    add_new_out_var_to_sub(n1)
                    if n1.PNode.Var == p2_var["v"]: 
                        n1.Exp = n1.Exp + p2_var["e"]
                        #45. Tips: SubList Node 底下的 POLY Node 的 對應的外部變數也必須同步更新 outExp. 
                        #          否則 之後 將節點轉 Formula 結果會對不上 Exp
                        for n1_sub_outvar in n1.Sub._outVarItems:
                            for i in range(len(t_PItems2VarItems)):
                                #DEBUG: print("================= n1_sub_outvar * t_PItems2VarItems[%s][v]= %s%s * %s%s"%(i, n1_sub_outvar["outVar"],
                                #    n1_sub_outvar["outExp"],t_PItems2VarItems[i]["v"],t_PItems2VarItems[i]["e"]))
                                
                                if n1_sub_outvar["outVar"] == t_PItems2VarItems[i]["v"]:
                                    if t_PItems2VarItems[i]["v"] == p2_var["v"]: 
                                        n1_sub_outvar["outExp"] = n1.Exp
                                        #DEBUG: print("GGGGGGG S.3 n1_sub_outvar['outVar']= %s, n1_sub_outvar['Exp'] = %s"%(
                                        #    n1_sub_outvar["outVar"],n1_sub_outvar["outExp"]))
                                        break
                        #45. End

                        #Tips: 下一個 Sub List Node
                        if n1.Next: back_sub_list.insert(0, n1.Next) 
                        n1 = n1.Sub if n1.Sub.Next else n1.Next
                    else: 
                        for n1_sub_outvar in n1.Sub._outVarItems:
                            for i in range(len(t_PItems2VarItems)):
                                #DEBUG: print("===============@@ n1_sub_outvar * t_PItems2VarItems[%s][v]= %s%s * %s%s"%(i, n1_sub_outvar["outVar"],
                                #    n1_sub_outvar["outExp"],t_PItems2VarItems[i]["v"],t_PItems2VarItems[i]["e"]))
                                if n1_sub_outvar["outVar"] == t_PItems2VarItems[i]["v"]:
                                    #Tips: 變數相同時才能將其 Exp 相加
                                    if t_PItems2VarItems[i]["v"] == p2_var["v"]: 
                                        n1_sub_outvar["outExp"] = n1_sub_outvar["outExp"] + t_PItems2VarItems[i]["e"]
                                        #DEBUG: print("GGGGGGG 3A n1_sub_outvar['outVar']= %s, n1_sub_outvar['outExp'] = %s"%(n1_sub_outvar["outVar"],n1_sub_outvar["outExp"]))
                                        break
                                    #Tips: 變數不同時不要將 Exp 相加 會 重複計算, 怕部分子變數Exp 仍未更新到, 強制更新為與其上層 SbuList Node.Exp 一樣
                                    else: pass
                        #Tips: 走過的 SubList Node 不再走, 儲存當下 SubList Node 的下一個 SubList, 
                        #      當該 Sublist Node 底下走訪完畢方能回到下一個未拜訪的 Sublist Node 位置 
                        if n1.Next: back_sub_list.insert(0, n1.Next) 
                        n1 = n1.Sub # Tips: 繼續搜尋下一層 變數
        #771. End
        #DEBUG: print("Result new_big_node = %s"%new_big_node.visit())
        new_big_nodes.append(new_big_node)

    PNode = new_big_nodes.pop(0)
    for i in range(len(new_big_nodes)): mergePolyItems(PNode, new_big_nodes[i])

    return PNode

def poly_to_formula(pnode:PolyNode, is_readable=False) -> str:
    """ 將 Poly Node 轉換成 多項式 數學 公式 字串. 
    
    Parameters
    ----------
    pnode: PolyNode
        要轉換成多項式數學公式字串的 Polynimal Node
        The polynimal node that will be coverted into a formula string.
        
    Returns
    -------
    formula: str
        回傳 轉換結果多項式公式字串
        return the coverted result of the Polynimal node for showing as a polynimal formula string.
    """

    if pnode.NodeType != PolyNodeType.POLY: raise Exception("[Invalid Value] the NodeType of 'PNode' should be PolyNodeType.POLY")
    current_node = pnode
    formula = ""
    item = ""
    loop = 0

    while current_node:
        loop += 1
        if current_node.NodeType == PolyNodeType.SUBLIST: 
            #DEBUG: print(current_node, current_node.Next, current_node.Sub, loop)
            item = poly_to_formula(current_node.Sub,is_readable)
        elif current_node.NodeType == PolyNodeType.ATOM: item = current_node.to_poly_item(is_readable)
        
        formula = formula + item
        current_node = current_node.Next
    
    #if is_readable and formula.startswith("+"): formula = formula[1:]
    #DEBUG: print(f"Formula: {formula}")
    return formula

def splitPolynomial(PnStr:str) -> list:
    """將多項式每一個項分割產生一個多項式的項組成的串列

    Parameters
    ----------
    PnStr: str
        要分割的多項式字串 
        The polynimal string that will be split into a polynomial items list.
        
    Returns
    -------
    PItems: list
        回傳 一個 由每一個多項式的項 所 組成的 字串陣列 
        return the splited list of the polynomial string.
    """

    s = normalized_item(PnStr)
    if s[0] not in ("+-") : s = '+' + s 
    TItems = s.split('+')
    if not TItems[0]: TItems.remove("")
    PItems = []
    for i in range(len(TItems)):
        if TItems[i][0] not in ("+-") : TItems[i] = '+' + TItems[i]
        if "-" in TItems[i]: 
            t = TItems[i].split("-")
            if t[0]=="": del t[0]
            for j in range(len(t)):
                #print("t[%d]= %s"%(j,t[j]))
                if t[j][0] not in '+' : PItems.append('-' + t[j])
                else: PItems.append(t[j])
        else: PItems.append(TItems[i])

    #print("PItems=", PItems)
    return PItems

def pnode_add_vars(varslist, pnode) -> PolyNode:
    """ 如果兩個要合併的多項式的項 其中一個項的變數量少於另一個項 則該項必須補足缺少的變數以利合併

    """
    
    sn = pn = None
    for v in varslist:
        sn = PolyNode(PolyNodeType.SUBLIST, exp=0, data=pnode)
        pn = PolyNode(PolyNodeType.POLY, data=v, next=sn)
        sn.PNode = pn
        pnode.Parent = sn
    return pn

def mergePolyItems(PolyItem1, PolyItem2) -> PolyNode:
        """合併兩個多項式的項並回傳合併結果 用於做 多項式 項跟項之間的加減
        """

        #"⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹"
        #pnode1 = item_string_to_pnode(normalized_item(PolyItem1))
        pn1 = poly_item_to_node(normalized_item(PolyItem1)) if isinstance(PolyItem1,str) else PolyItem1
        #pnode2 = item_string_to_pnode(normalized_item(PolyItem2))
        pn2 = poly_item_to_node(normalized_item(PolyItem2)) if isinstance(PolyItem2,str) else PolyItem2
        # return pnode = pnode1 + pnode2
        n1=pn1; n2=pn2; pren1=pren2=None; prepren1=prepren2=None
        pn1_add_vars = [] 
        pn2_add_vars = [] #如果 pn2 變數少於 pn1, 則 pn2 需要補足缺少的變數
        pn1cv = get_poly_item_coef_and_vars(PolyItem1) if isinstance(PolyItem1,str) else {"vars":[],"coef": 0.0}
        pn2cv = get_poly_item_coef_and_vars(PolyItem2) if isinstance(PolyItem2,str) else {"vars":[],"coef": 0.0}
       
        while(n1 and n2):
            pn = None; n = None
            if (n1.NodeType == n2.NodeType == PolyNodeType.POLY):
                if n1.Var == n2.Var:
                    # 2456 Tips: New Add pn2 adds out vars, then compare pn1/pn2 again
                    if pn2_add_vars: 
                        pn2 = pnode_add_vars(pn2_add_vars, pn2)
                        prepren1=pren1.PNode; n1=pren1; pren1 = prepren1; n2=pn2.Next; pren2 = pn2
                        prepren2=None; pn2_add_vars = []; continue
                    # 2456. End
                    pren1=n1; pren2=n2
                    n1=n1.Next; n2=n2.Next; continue # Tips: 繼續往下 檢查
                elif n1.Var > n2.Var: # Tips: pn2 的變數比 pn1 少
                    # Tips: 如果 n1. n2 都只有一個變數, 則直接把 n2 插入到 n1 作為新的 Sub List Node 尾端, 且 n1 Poly 得把其後的 ATOM 降到 Sub List Level 底下
                    if len(pn1cv["vars"]) == len(pn2cv["vars"]) == 1:
                        n1_ptr = n1
                        copy_n1 = copy.deepcopy(n1)
                        while n1_ptr and n1_ptr.Next:
                            new_n1_sn=None; new_n1_sn_sub=None; new_atom = None
                            new_n1_sn_sub = PolyNode(PolyNodeType.POLY, data=n2.Var, pnode=n1)
                            new_n1_sn = PolyNode(PolyNodeType.SUBLIST, exp=n1_ptr.Next.Exp, data=new_n1_sn_sub, pnode=n1)
                            if n1_ptr == n1: n1.Next = new_n1_sn; 
                            new_n1_sn_sub.Parent = new_n1_sn
                            n1_ptr = n1
                            n1_sub_ptr = new_n1_sn_sub
                            tn1_ptr = copy_n1
                            while tn1_ptr.Next:
                                new_atom = PolyNode(PolyNodeType.ATOM, var=n2.Var, data=tn1_ptr.Next.Coef, pnode=new_n1_sn_sub)
                                n1_sub_ptr.Next = new_atom
                                n1_sub_ptr = n1_sub_ptr.Next
                                tn1_ptr = tn1_ptr.Next
                            n1_ptr = n1_ptr.Next
                        
                        new_n1_n2sn = PolyNode(PolyNodeType.SUBLIST, exp=0, data=n2, pnode=n1)
                        n1_ptr.Next = new_n1_n2sn
                        n2.Parent = new_n1_n2sn
                        del copy_n1
                        break
                    else:
                        pn2_add_vars.insert(0,n1.Var)
                        if pren1: prepren1 = pren1
                        n1=n1.Next; pren1=n1; n1=n1.Sub; continue
                else: # Tips: pn2 的變數比 pn1 多
                    tmpn1 = tmpn2 = None
                    pn=pn1; pn1=pn2; pn2=pn
                    tmpn1 = prepren1; prepren1 = prepren2; prepren2 = tmpn1
                    tmpn2 = pren1; pren1 = pren2; pren2 = tmpn2
                    n=n1; n1=n2; n2=n
                    continue

            if (n1.NodeType == n2.NodeType == PolyNodeType.SUBLIST):
                #1. Tips: Case 1 - Insert SubList
                if n1.Exp > n2.Exp: 
                    if n1.Next: n1 = n1.Next
                    else: n1.Next = n2; pn2.Next = None; break
                elif n1.Exp < n2.Exp: 
                    if n1.PNode.Var == n2.PNode.Var:
                        pn=pn1; pn1=pn2; pn2=pn; 
                        n=n1; n1=n2; n2=n
                        if n1.Next: n2.Next = n1; pren1.Next = n2; n1.Next = n2; pren2.Next = None; break 
                    else: print("Something Logic Error!!!!!!!!!!"); break 
                else:
                    pren1 = n1; pren2 = n2
                    n1=n1.Sub; n2=n2.Sub; continue # Tips: 繼續往下 檢查
            if (n1.NodeType == n2.NodeType == PolyNodeType.ATOM):
                if n1.Exp > n2.Exp: n1.Next = n2; pn2.Next = None; break
                elif n1.Exp < n2.Exp: 
                    pn=pn1; pn1=pn2; pn2=pn; 
                    n=n1; n1=n2; n2=n
                    n1.Next = n2; pn2.Next = None; break
                else: 
                    n1.Coef += n2.Coef 
                    pren2=n2; n2=n2.Next; continue # Tips: 繼續往下 檢查
                
        f = poly_to_formula(pn1)
        f = f[1:] if f.startswith("+") else f
        print(f"F(X,Y) = {f}")
        return pn1

def polyFormulaToNode(formula):
        """ 將多項式字串/多項式項目串列 轉換為 PolyNode 
        """

        pItems = None
        if type(formula).__name__ == "str": pItems = splitPolynomial(formula)
        else: pItems = formula

        pn1 = pItems[0]
        for i in range(len(pItems)):
            if i==0: continue
            pn2 = pItems[i]
            #DEBUG: print(f"pn1, pn2 = {pn1},{pn2}")
            #Tips: Merge pn2 into pn1, 以 pn1 為主
            pn1 = mergePolyItems(pn1,pn2)
        
        #DEBUG: print("pn1 = ", pn1)
        pn1 = poly_item_to_node(pItems[0]) if len(pItems)==1 else pn1
        f = poly_to_formula(pn1)
        f = f[1:] if f.startswith("+") else f
        #DEBUG: print(f"[polyFormulaToNode] F = {f}, visit={pn1.visit()}")
        return pn1
        
def normalized_item(pItem:str):
    """ normalized a polynimal item for parsing. """

    sup_list = ["⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹"]
    nItem = ""
    i = 0
    #DEBUG: print("Test Item =", pItem)
    while (i<len(pItem)):
        if i==0 and pItem[i] == '+': pass
        elif pItem[i].isdigit() or pItem[i] in ".-": nItem += pItem[i]
        else:
            if i < (len(pItem) - 1) :
                nItem = (nItem + pItem[i] + digits_to_sup("1")) if (pItem[i+1].isalpha()) else (nItem + pItem[i])
            else: nItem += pItem[i] + digits_to_sup("1")
        i += 1
    result = nItem
    if nItem[0].isalpha(): result = "1.0" + nItem
    if nItem[0].isdigit(): result = nItem
    if nItem[0] == '-' and nItem[1].isdigit(): result = nItem
    if nItem[0] == '-' and nItem[1].isalpha(): result = "-1.0" + nItem[1:]

    return result

def get_poly_item_coef_and_vars(PItem:str) -> dict:
    """ 輸入單一多項式項 然後分析回傳該項的 係數和變數串. 

    Parameters
    ----------
    PItem: str
        要分析的 多項式項 的 字串, 例如: 5.3A²P²X².
        The string of a polynimal item that will be parsed to generate coef and vars list.
        For Example, 5.3A²P²X².
        
    Returns
    -------
    result: dict
        回傳 分析結果 為一個 由兩個元素組成的 dict, (1).coef: 分析項的係數 (2). vars: 分析項的變數串陣列.
        return the dict of a result contains the coef and vars list of the polynimal item we parse.
    """
    
    result = {"coef":0.0, "vars":[]}
    
    normal_p_item = normalized_item(PItem)
    #DEBUG: print(f"[poly_item_to_node] t = {normal_p_item}")
    coef_str = ""

    #327. Tips: Get Coef
    for i in range(len(normal_p_item)):
        if (normal_p_item[i].isdigit() or normal_p_item[i] in "-."): coef_str += normal_p_item[i]; continue
        result["coef"] = float(coef_str)
        break
    #327. End

    #328. Tips: collect all vars in an item
    for i in range(len(normal_p_item)):
        var_item =  {"v":"","e":""}
        if normal_p_item[i].isalpha(): 
            var_item["v"] = normal_p_item[i]
            var_exp = ""
            while i+1 < len(normal_p_item):
                if not normal_p_item[i+1].isalpha(): 
                    var_exp += normal_p_item[i+1]; i += 1
                    if i == len(normal_p_item)-1:
                        var_item["e"] = sup_to_digits(var_exp); break
                else: 
                    var_item["e"] = sup_to_digits(var_exp); break
            result["vars"].insert(0,var_item)
    #328. End

    if not result["vars"]: 
        result["vars"].insert(0,{"v":"X", "e":0})
        result["coef"] = float(PItem)

    return result

def poly_item_to_node(pItem:str):
    """ Parse a polynimal item to a poly node

    For Example : -7.22X⁷Z⁶
    pn1(var = Z,[]) -> pn1_s1(exp = 6) -> Null
                          |
                    pn1_s1_pn1(Var = Y,[Z]) -> pn1_s1_pn1_s1(exp = 1) -> Null
                                                      |
                                           pn1_s1_pn1_s1_pn(Var = X) -> node(-7.22,X,7)

    0 pn[0]:Z -> sn[0]:6 -> Null
                  |
    1            pn[1]:Y -> sn[1]:1 -> Null
                             |
    2                       pn[2]:X -> node(-7.22,X,7)
    """

    t_item = get_poly_item_coef_and_vars(pItem)
    item_coef = t_item["coef"]
    vars_list = t_item["vars"]
    
    #DEBUG: print (f"vars_list = {vars_list} , item_coef = {coef_str} ")
    pn_list = []
    sn_list = []

    for i in range(len(vars_list)):
        pn = None
        sn = None
        node = None

        #123. Tips: 當 pnode 後面直接接 ATOM Node
        if (len(vars_list) == 1):
            pn = PolyNode(PolyNodeType.POLY, data=vars_list[i]["v"])
            node = PolyNode(PolyNodeType.ATOM, exp=vars_list[i]["e"], data=item_coef, pnode=pn)
            pn.Next = node
            pn_list.append(pn)
            break
        #123. END

        if i == 0:
            #676. Tips: Generate the first Vars Node: P(v) --> S(e), then add them into PNode&SubListNode List
            pn = PolyNode(PolyNodeType.POLY, data=vars_list[i]["v"])
            sn = PolyNode(PolyNodeType.SUBLIST, exp=vars_list[i]["e"], data=None, pnode=pn)
            pn.Next = sn
            pn_list.append(pn)
            sn_list.append(sn)
            #676. End
        else:
            #Tips: 每一個 var 變數必然對應一個起始的 PNode 
            pn = PolyNode(PolyNodeType.POLY, data=vars_list[i]["v"], parent = sn_list[i-1])
            pn_list.append(pn)

            # Tips: 最後一個 var 變數必然是 ATOM 的 Var
            if i == len(vars_list)-1:
                node = PolyNode(PolyNodeType.ATOM, exp=vars_list[i]["e"], data=item_coef, pnode=pn_list[i])
                # append the atom node into its POLY Node
                pn_list[i].Next = node
                sn_list[i-1].Sub = pn_list[i]
            else:
                sn = PolyNode(PolyNodeType.SUBLIST, exp=vars_list[i]["e"], data=None, pnode=pn_list[i])
                sn_list.append(sn)
                pn_list[i].Next = sn_list[i]
                sn_list[i-1].Sub = pn_list[i]

    #DEBUG: print("Formula: ", poly_to_formula(pn_list[0]))
    return pn_list[0]
    
#Tips: Covert an integer into a superscript(sup) string
def digits_to_sup(digits:int) -> str:
        """ Covert an integer into a superscript(sup) string. """
        #Tips: Another List Format: ["⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹"]
        superscripts = ["\u2070", "\u00b9", "\u00b2", "\u00b3", "\u2074", "\u2075", "\u2076", "\u2077", "\u2078", "\u2079"]
        return ''.join([superscripts[int(digit_char)] for digit_char in str(digits)])

def sup_to_digits(sups:str) -> int:
        """ Covert a superscript(sup) string into an integer. """
        #Tips: Another List Format: ["⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹"]
        anit_superscripts = {"\u2070":"0","\u00b9":"1","\u00b2":"2","\u00b3":"3","\u2074":"4",
                             "\u2075":"5","\u2076":"6","\u2077":"7","\u2078":"8","\u2079":"9"}
        digits = ''.join([anit_superscripts[sup_char] for sup_char in sups])
        return int(digits)

if __name__ == "__main__":

    #["⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹"]
    #mergePolyItems()
    #splitPolynomial()
    #node = polyFormulaToNode()
    #print(node.visit())
    #poly_item_to_node("-3X⁶")
    #node = multiplyPolynomial("4YZ+5Y⁴Z⁴","2XZ⁹")
    #print(node.visit())
    #print("Formula: 4XY+5X⁴Y⁴ * 2X⁹Y⁹ = 8X¹⁰Y¹⁰ + 10X¹³Y¹³")
    #print("Formula: 4XZ * 2YZ⁹ = 8XYZ¹⁰")
    
    node = multiplyPolynomial("4EXZ","2YZ⁹")
    print("Formula: 4EXZ * 2YZ⁹ = 8EXYZ¹⁰")
    #node = multiplyPolynomial("5X⁵Y²+2XY+7","10Y⁶")
    #print("Formula: (5X⁵Y²+2XY+7) * 10Y⁶ = 50X⁵Y⁸+20.0XY⁷+70Y⁶")
    #node = multiplyPolynomial("5X⁵Y²+2XY","10Y⁶+3X")
    #print("Formula: (5X⁵Y²+2XY) * (10Y⁶+3X) = 50X⁵Y⁸+20XY⁷+15X⁶Y²+6X²Y")
    #node = multiplyPolynomial("5X⁵Y²","10Y⁶")
    #print("Formula: 5X⁵Y² * 10Y⁶ = 50X⁵Y⁸")
    #node = multiplyPolynomial("5X⁵Y²+2XY","10Y⁶")
    #print("Formula: (5X⁵Y²+2XY) * 10Y⁶ = 50X⁵Y⁸+20.0XY⁷")
    #node = multiplyPolynomial("10XY⁶+3XY","5X⁵")
    #print("Formula: (10XY⁶+3XY) * 5X⁵ = 50X⁶Y⁶+15X⁶Y")
    #node = multiplyPolynomial("5X⁵Y²+3XY⁹","10Y⁶")
    #print("Formula: (5X⁵Y²+2XY+7) * 10Y⁶ = 50X⁵Y⁸+20.0XY⁷+70Y⁶")
    print(poly_to_formula(node))
    print("@"*20 + "\nnode:    " + node.visit())


