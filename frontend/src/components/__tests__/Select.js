import React from "react";
import chai from "chai";
import {render} from "enzyme";

import Select from "../../components/Select"


let expect = chai.expect;

describe("Select Component", function(){

    it("should generate a list of 3 options.", function(){
        let SelectTest = class extends Select {
            componentWillMount() {
                this.setState({
                    options: [
                        {"id": 1, "city": "Nilópolis"},
                        {"id": 2, "city": "Olária"},
                    ]
                })
            }
        }

        const select = render(<SelectTest label="City" name="city" target="city"/>);
        const options = select.find("option");

        expect(options.length).to.equal(3);

        expect(options.first().text()).to.equal("Selecione uma opção");
        expect(options.last().text()).to.equal("Olária");
    })
});
