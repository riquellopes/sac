import React from "react";
import chai from "chai";
import {render} from "enzyme";

import Row from "../../components/Row"


let expect = chai.expect;

describe("Row Component", function(){
    let row = {
        "id": 1,
        "text": "xxxx",
        "created_date": "2017-08-13T04:24:25.872240+00:00",
        "type": {
            type: 1
        },
        "reason": {
            reason: 1
        },
        "country": {
            country: 1
        }
    }

    it("renders without problems.", function(){
        const wrapper = render(
            <Row {...row}/>
        )
        expect(wrapper).to.exist;
    });

    it("first element of td should be 1.", function(){
        const wrapper = render(
            <Row {...row}/>
        )

        expect(wrapper.find("td").first().text()).to.equal('1');
    });

    it("last element of td should be a date.", function(){
        const wrapper = render(
            <Row {...row}/>
        )

        expect(wrapper.find("td").last().text()).to.equal("2017-8-13 04:24:25");
    });
})
